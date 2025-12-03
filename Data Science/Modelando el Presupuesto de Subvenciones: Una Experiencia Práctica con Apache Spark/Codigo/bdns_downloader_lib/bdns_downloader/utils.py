import os, json, math, time, random, glob, asyncio
from pathlib import Path
from typing import Iterable

import requests
import aiohttp
from aiohttp import ClientOSError, ServerDisconnectedError, ClientResponseError, ContentTypeError

from .config import (
    CABECERAS_DEFAULT,
    TAM_PAGINA_DEFAULT,
    REINTENTOS_SYNC_DEFAULT,
    TIMEOUT_SYNC_SEG_DEFAULT,
    ESPERA_BASE_DEFAULT,
    MAX_FICHERO_BYTES_DEFAULT,
    LOG_CADA_DEFAULT,
    MICRO_PAUSA_S_DEFAULT,
    REINTENTOS_ASYNC_DEFAULT,
)

def extraer_numconv(obj: dict):
    return (
        obj.get("numConv")
        or obj.get("numeroConvocatoria")
        or obj.get("numeroConv")
        or obj.get("id")
    )

def get_json_robusto(
    url: str,
    params: dict | None = None,
    intento: int = 1,
    *,
    headers: dict | None = None,
    reintentos: int = REINTENTOS_SYNC_DEFAULT,
    timeout_seg: int = TIMEOUT_SYNC_SEG_DEFAULT,
    espera_base: float = ESPERA_BASE_DEFAULT,
):
    headers = headers or CABECERAS_DEFAULT
    try:
        r = requests.get(url, params=params, headers=headers, timeout=timeout_seg)
        if r.status_code in (429, 500, 502, 503, 504) and intento <= reintentos:
            espera = espera_base * (2 ** (intento - 1)) * (1.0 + 0.25 * random.random())
            time.sleep(espera)
            return get_json_robusto(
                url,
                params,
                intento + 1,
                headers=headers,
                reintentos=reintentos,
                timeout_seg=timeout_seg,
                espera_base=espera_base,
            )
        r.raise_for_status()
        return r.json()
    except Exception:
        if intento <= reintentos:
            espera = espera_base * (2 ** (intento - 1)) * (1.0 + 0.25 * random.random())
            time.sleep(espera)
            return get_json_robusto(
                url,
                params,
                intento + 1,
                headers=headers,
                reintentos=reintentos,
                timeout_seg=timeout_seg,
                espera_base=espera_base,
            )
        raise

def leer_ids_desde_indice(ruta: Path) -> list[str]:
    ids = []
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el índice: {ruta}")
    with ruta.open("r", encoding="utf-8") as f:
        for linea in f:
            try:
                obj = json.loads(linea)
                k = extraer_numconv(obj)
                if k is not None:
                    ids.append(str(k).strip())
            except Exception:
                continue
    return ids

def leer_ids_procesados_rotativos(patron_archivos: str) -> set[str]:
    procesados = set()
    for ruta in sorted(glob.glob(patron_archivos)):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        obj = json.loads(linea)
                        k = extraer_numconv(obj)
                        if k is not None:
                            procesados.add(str(k).strip())
                    except Exception:
                        continue
        except FileNotFoundError:
            continue
    return procesados

def obtener_siguiente_indice_archivo(carpeta: Path, prefijo: str, ext: str, patron: str):
    archivos = sorted(glob.glob(patron))
    if not archivos:
        idx = 1
        ruta = carpeta / f"{prefijo}{idx:04d}{ext}"
        return idx, 0, ruta
    ultimo = archivos[-1]
    idx = int(Path(ultimo).stem.replace(prefijo, ""))
    tam = os.path.getsize(ultimo)
    return idx, tam, Path(ultimo)

class EscritorRotativoNDJSON:
    def __init__(self, carpeta: Path, prefijo: str, ext: str, max_bytes: int, patron: str):
        self.carpeta = carpeta
        self.prefijo = prefijo
        self.ext = ext
        self.max_bytes = max_bytes
        self.patron = patron
        self.idx, self.tam, self.ruta = obtener_siguiente_indice_archivo(
            carpeta, prefijo, ext, patron
        )
        self.f = open(self.ruta, "a", encoding="utf-8")

    def _rotar(self):
        try:
            self.f.close()
        except Exception:
            pass
        self.idx += 1
        self.ruta = self.carpeta / f"{self.prefijo}{self.idx:04d}{self.ext}"
        self.f = open(self.ruta, "a", encoding="utf-8")
        self.tam = 0
        print(f"🗂️  Rotando a nuevo fichero: {self.ruta.name}")

    def escribir(self, obj: dict):
        linea = json.dumps(obj, ensure_ascii=False) + "\n"
        bytes_linea = len(linea.encode("utf-8"))
        if self.tam + bytes_linea > self.max_bytes:
            self._rotar()
        self.f.write(linea)
        self.tam += bytes_linea

    def cerrar(self):
        try:
            self.f.close()
        except Exception:
            pass

async def fetch_json_async(
    session: aiohttp.ClientSession,
    params: dict,
    intento: int = 1,
    *,
    reintentos: int = REINTENTOS_ASYNC_DEFAULT,
    espera_base: float = ESPERA_BASE_DEFAULT,
):
    try:
        async with session.get(session._base_url, params=params) as r:  # ver uso en detalle.py
            if r.status in (429, 500, 502, 503, 504) and intento <= reintentos:
                espera = espera_base * (2 ** (intento - 1)) * (1 + 0.25 * random.random())
                await asyncio.sleep(espera)
                return await fetch_json_async(
                    session, params, intento + 1, reintentos=reintentos, espera_base=espera_base
                )
            r.raise_for_status()
            return await r.json()
    except (asyncio.TimeoutError, ClientOSError, ServerDisconnectedError, ContentTypeError, ClientResponseError):
        if intento <= reintentos:
            espera = espera_base * (2 ** (intento - 1)) * (1 + 0.25 * random.random())
            await asyncio.sleep(espera)
            return await fetch_json_async(
                session, params, intento + 1, reintentos=reintentos, espera_base=espera_base
            )
        raise
