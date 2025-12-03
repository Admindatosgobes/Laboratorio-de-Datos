from pathlib import Path
import aiohttp

# Valores por defecto (puedes sobreescribirlos al llamar a las funciones públicas)
BASE_API_DEFAULT = "https://www.infosubvenciones.es/bdnstrans/api"
CARPETA_SALIDA_DEFAULT = Path("data/bdns")

CABECERAS_DEFAULT = {
    "accept": "application/json",
    "user-agent": "bdns-descarga-educativa/1.0",
}

TAM_PAGINA_DEFAULT = 1000
REINTENTOS_SYNC_DEFAULT = 5
TIMEOUT_SYNC_SEG_DEFAULT = 60
ESPERA_BASE_DEFAULT = 1.2

FILTROS_BUSQUEDA_DEFAULT = {
    "order": "numeroConvocatoria",
    "direccion": "asc",
}

MAX_CONCURRENCIA_DEFAULT = 10
REINTENTOS_ASYNC_DEFAULT = 6
TIMEOUTS_ASYNC_DEFAULT = aiohttp.ClientTimeout(total=120, connect=30, sock_read=90)

LOG_CADA_DEFAULT = 200
MICRO_PAUSA_S_DEFAULT = 0.02

MAX_FICHERO_MB_DEFAULT = 100
MAX_FICHERO_BYTES_DEFAULT = MAX_FICHERO_MB_DEFAULT * 1024 * 1024