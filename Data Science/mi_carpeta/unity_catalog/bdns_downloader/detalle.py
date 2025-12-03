from pathlib import Path
import asyncio
import glob

import aiohttp

from .config import (
    CARPETA_SALIDA_DEFAULT,
    BASE_API_DEFAULT,
    CABECERAS_DEFAULT,
    MAX_CONCURRENCIA_DEFAULT,
    TIMEOUTS_ASYNC_DEFAULT,
    LOG_CADA_DEFAULT,
    MICRO_PAUSA_S_DEFAULT,
    MAX_FICHERO_BYTES_DEFAULT,
)
from .utils import (
    leer_ids_desde_indice,
    leer_ids_procesados_rotativos,
    EscritorRotativoNDJSON,
    fetch_json_async,
)

async def _productor_detalles(session, sem, cola, ids, micro_pausa_s: float):
    async def tarea(num_conv: str):
        async with sem:
            datos = await fetch_json_async(session, {"numConv": num_conv})
            if isinstance(datos, list):
                for d in datos:
                    await cola.put(d)
            else:
                await cola.put(datos)
            await asyncio.sleep(micro_pausa_s)
    await asyncio.gather(*(tarea(i) for i in ids))
    await cola.put(None)

async def _consumidor_escritor(cola, escritor_rot: EscritorRotativoNDJSON, cada_n: int):
    cont = 0
    try:
        while True:
            item = await cola.get()
            if item is None:
                break
            try:
                escritor_rot.escribir(item)
                cont += 1
                if cont % cada_n == 0:
                    print(
                        f"💾 Detalles escritos en esta sesión: {cont} | "
                        f"Archivo actual: {escritor_rot.ruta.name} "
                        f"({escritor_rot.tam/1024/1024:.1f} MB)"
                    )
            except Exception:
                continue
    finally:
        escritor_rot.cerrar()
        print(
            f"✅ Sesión de escritura cerrada. Total nuevos: {cont} | "
            f"Último fichero: {escritor_rot.ruta.name}"
        )

def preparar_ids_detalle(
    carpeta_salida: Path | str = CARPETA_SALIDA_DEFAULT,
    *,
    limite_ids_detalle: int | None = None,
):
    carpeta_salida = Path(carpeta_salida)
    fichero_indice = carpeta_salida / "convocatorias_indice.ndjson"
    prefijo_detalle = "convocatorias_detalle_"
    ext_detalle = ".ndjson"
    patron_detalle = str(carpeta_salida / f"{prefijo_detalle}*{ext_detalle}")

    print("▶️ Paso 1/3 — Leyendo IDs desde el índice…")
    todos = leer_ids_desde_indice(fichero_indice)

    print("▶️ Paso 2/3 — Detectando IDs ya guardados en detalle (archivos rotativos)…")
    ya = leer_ids_procesados_rotativos(patron_detalle)

    pendientes = [i for i in todos if i not in ya]
    if limite_ids_detalle is not None:
        pendientes = pendientes[:limite_ids_detalle]

    print(f"🧾 IDs totales en índice: {len(todos)} | Ya guardados: {len(ya)} | Pendientes: {len(pendientes)}")
    return {
        "todos": todos,
        "ya_procesados": ya,
        "pendientes": pendientes,
        "patron_detalle": patron_detalle,
        "prefijo_detalle": prefijo_detalle,
        "ext_detalle": ext_detalle,
    }

async def descargar_detalle_async(
    carpeta_salida: Path | str = CARPETA_SALIDA_DEFAULT,
    *,
    base_api: str = BASE_API_DEFAULT,
    limite_ids_detalle: int | None = None,
    max_concurrencia: int = MAX_CONCURRENCIA_DEFAULT,
    timeouts_async: aiohttp.ClientTimeout = TIMEOUTS_ASYNC_DEFAULT,
    log_cada: int = LOG_CADA_DEFAULT,
    micro_pausa_s: float = MICRO_PAUSA_S_DEFAULT,
    max_fichero_bytes: int = MAX_FICHERO_BYTES_DEFAULT,
):
    carpeta_salida = Path(carpeta_salida)
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    info = preparar_ids_detalle(carpeta_salida, limite_ids_detalle=limite_ids_detalle)
    pendientes = info["pendientes"]
    if not pendientes:
        print("✅ No hay pendientes de detalle. Nada que hacer.")
        return

    patron_detalle = info["patron_detalle"]
    prefijo_detalle = info["prefijo_detalle"]
    ext_detalle = info["ext_detalle"]

    connector = aiohttp.TCPConnector(
        limit=max_concurrencia * 4,
        limit_per_host=max(6, max_concurrencia // 2),
        enable_cleanup_closed=True,
        ttl_dns_cache=300,
    )
    sem = asyncio.Semaphore(max_concurrencia)
    cola = asyncio.Queue(maxsize=max_concurrencia * 4)
    escritor_rot = EscritorRotativoNDJSON(
        carpeta_salida,
        prefijo_detalle,
        ext_detalle,
        max_fichero_bytes,
        patron_detalle,
    )

    async with aiohttp.ClientSession(
        timeout=timeouts_async,
        connector=connector,
        headers=CABECERAS_DEFAULT,
        base_url=f"{base_api}/convocatorias/",
    ) as session:
        # pequeño truco: fetch_json_async usa session._base_url
        session._base_url = f"{base_api}/convocatorias/"
        prod = asyncio.create_task(_productor_detalles(session, sem, cola, pendientes, micro_pausa_s))
        cons = asyncio.create_task(_consumidor_escritor(cola, escritor_rot, log_cada))
        await asyncio.gather(prod, cons)
