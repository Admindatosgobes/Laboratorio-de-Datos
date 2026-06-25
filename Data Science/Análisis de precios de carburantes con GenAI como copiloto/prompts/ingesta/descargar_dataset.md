# Prompt: Descargar Dataset de Precios de Carburantes

## Prompt Original

```
Necesito descargar datos públicos de "Precios de Carburantes en las Gasolineras Españolas"
desde la API del Ministerio de Turismo. El API tiene particularidades:
- URL: https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/
- Método: GET (sin parámetros)
- Respuesta: JSON con estructura {Fecha, ResultadoConsulta, ListaEESSPrecio: []}
- Separadores de decimales europeos (,) en precios y coordenadas
- Ocasionales problemas de SSL que requieren verify=False

Escribe código Python robusto que:

1. Descargue los datos en JSON desde la URL (método GET)
2. Maneje fallos de SSL (usa verify=False en requests, -k en curl)
3. Implemente fallback: si falla requests, intenta curl -k
4. Si ambos fallan, retorna estructura JSON vacía (notebook generará datos demo)
5. Convierte separadores decimales (,) a formato Python (.)
6. Verifique que el dataframe tiene ~11k filas (o 0 si usa fallback)
7. Muestre mensajes claros en español

El código debe ser simple, robusto, y funcionar en Google Colab sin configuración previa.
```

## Resultado Obtenido

La solución implementó triple fallback:

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import subprocess
import json

def descargar_datos_api(url):
 # Intento 1: requests con verify=False
 try:
 print(" Intentando con requests...")
 sesion = requests.Session()
 sesion.headers.update({"Accept": "application/json"})
 reintentos = Retry(total=2, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
 sesion.mount("https://", HTTPAdapter(max_retries=reintentos))
 
 response = sesion.get(url, timeout=45, verify=False)
 response.raise_for_status()
 print(" OK con requests")
 return response.json()
 except Exception as e:
 print(f" requests falló: {type(e).__name__}")

 # Intento 2: curl con -k (insecure)
 try:
 print(" Intentando con curl (insecure)...")
 resultado = subprocess.run(
 ["curl", "-s", "-L", "-k", "--max-time", "60",
 "-H", "Accept: application/json", url],
 capture_output=True, text=True, timeout=75
 )
 if resultado.returncode == 0 and resultado.stdout.strip():
 print(" OK con curl")
 return json.loads(resultado.stdout)
 except Exception as e:
 print(f" curl falló: {type(e).__name__}")

 # Fallback: estructura vacía
 print(" ⚠ API no disponible. Datos demo serán usados.")
 return {"Fecha": "N/A", "ResultadoConsulta": "SIN_CONEXION", "ListaEESSPrecio": []}

# Usar la función
url_api = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"
datos_json = descargar_datos_api(url_api)

# Procesar JSON a DataFrame
df_raw = pd.DataFrame(datos_json.get('ListaEESSPrecio', []))
if len(df_raw) == 0:
 print("⚠ Generando datos de demostración (11,000 gasolineras)...")
 # ... generar datos demo ...
else:
 print(f" Dataset descargado: {len(df_raw)} filas desde API")
```

## Reflexión

**Qué funcionó bien:**
- El triple fallback (requests → curl → fallback vacío) garantiza que el notebook siempre funciona
- `verify=False` resuelve problemas de SSL del servidor
- Mapeo automático de columnas JSON a nombres estándar internos
- Separadores decimales se convierten automáticamente en el procesamiento

**Qué aprendimos:**
- El API del Ministerio a veces tiene problemas de certificados SSL
- `requests` + `verify=False` es más simple que workarounds de certificados
- El fallback a datos demo sintéticos es mejor que dejar que el notebook falle
- Implementar fallback es clave para la reproducibilidad en Colab (ambiente inconsistente)

**Patrón reutilizable:**
- Aplicable a cualquier API con problemas de SSL (muchas APIs españolas públicas)
- Patrón: intentar método robusto → fallback simple → fallback datos demo
- Siempre retornar estructura válida, nunca excepciones sin manejo
- Datos demo deben ser lo suficientemente realistas para la pipeline
