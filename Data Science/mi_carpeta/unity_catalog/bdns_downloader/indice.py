from pathlib import Path
import json, math

from .config import (
    CARPETA_SALIDA_DEFAULT,
    BASE_API_DEFAULT,
    TAM_PAGINA_DEFAULT,
    FILTROS_BUSQUEDA_DEFAULT,
)
from .utils import get_json_robusto

def descargar_indice_reanudable(
    carpeta_salida: Path | str = CARPETA_SALIDA_DEFAULT,
    *,
    base_api: str = BASE_API_DEFAULT,
    filtros_busqueda: dict | None = None,
    tam_pagina: int = TAM_PAGINA_DEFAULT,
    limite_paginas_descarga: int | None = None,
    saltar_descarga_indice: bool = True,
):
    carpeta_salida = Path(carpeta_salida)
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    fichero_indice = carpeta_salida / "convocatorias_indice.ndjson"
    progreso_paginas = carpeta_salida / "progreso_paginas.txt"
    progreso_meta = carpeta_salida / "meta_indice.json"

    filtros = {**FILTROS_BUSQUEDA_DEFAULT, **(filtros_busqueda or {})}

    url_indice = f"{base_api}/convocatorias/busqueda"

    def guardar_progreso_pagina(n_pagina: int):
        progreso_paginas.write_text(str(n_pagina), encoding="utf-8")

    def cargar_progreso_pagina() -> int:
        if progreso_paginas.exists():
            try:
                return int(progreso_paginas.read_text(encoding="utf-8").strip())
            except Exception:
                return 0
        return 0

    def guardar_meta_indice(meta: dict):
        progreso_meta.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    def leer_meta_indice() -> dict | None:
        if progreso_meta.exists():
            try:
                return json.loads(progreso_meta.read_text(encoding="utf-8"))
            except Exception:
                return None
        return None

    if saltar_descarga_indice and fichero_indice.exists():
        print("🟡 Omitiendo descarga del índice (SALTAR_DESCARGA_INDICE=True y existe el fichero).")
        return fichero_indice

    meta = leer_meta_indice()
    if meta is None:
        params_0 = {"page": 0, "pageSize": tam_pagina, **filtros}
        primera = get_json_robusto(url_indice, params=params_0)
        content = primera.get("content", primera if isinstance(primera, list) else [])
        total_elements = primera.get("totalElements") or len(content)
        total_pages = primera.get("totalPages") or math.ceil(total_elements / tam_pagina)

        with fichero_indice.open("a", encoding="utf-8") as f:
            for it in content:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")

        meta = {
            "totalElements": total_elements,
            "totalPages": total_pages,
            "pageSize": tam_pagina,
            "filtros": filtros,
        }
        guardar_meta_indice(meta)
        guardar_progreso_pagina(0)
        print(f"🟢 Índice: descargada página 0 | totalPages={total_pages} | totalElements={total_elements}")
    else:
        print(f"ℹ️ Meta índice existente: totalPages={meta.get('totalPages')} | pageSize={meta.get('pageSize')}")

    total_pages = meta["totalPages"]
    if limite_paginas_descarga is not None:
        total_pages = min(total_pages, limite_paginas_descarga)

    start_page = cargar_progreso_pagina() + 1
    if start_page >= total_pages:
        print("✅ Índice ya estaba completo. Nada que descargar.")
        return fichero_indice

    for page in range(start_page, total_pages):
        params = {"page": page, "pageSize": tam_pagina, **filtros}
        bloque = get_json_robusto(url_indice, params=params)
        content = bloque.get("content", bloque if isinstance(bloque, list) else [])
        if not content:
            print(f"⚠️ Página {page} sin contenido. Detengo índice aquí.")
            guardar_progreso_pagina(page)
            break

        with fichero_indice.open("a", encoding="utf-8") as f:
            for it in content:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")

        guardar_progreso_pagina(page)
        if page % 10 == 0:
            print(f"💾 Índice: guardada página {page}/{total_pages-1}")

    print("✅ Descarga del índice completada (reanudable).")
    return fichero_indice
