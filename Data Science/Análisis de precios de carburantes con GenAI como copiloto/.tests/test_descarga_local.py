#!/usr/bin/env python3
"""
Script de prueba local para verificar la descarga y procesamiento de datos.
Simula lo que hace el notebook en Colab.
"""

import json
import pandas as pd
import numpy as np
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import subprocess

def descargar_datos_api(url):
    """Descarga datos con triple fallback"""
    # Configurar sesión robusta
    sesion = requests.Session()
    sesion.headers.update({
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })
    reintentos = Retry(total=3, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
    sesion.mount("https://", HTTPAdapter(max_retries=reintentos))

    # Intento 1: requests
    try:
        print("  Intentando con requests...")
        response = sesion.get(url, timeout=30, verify=False)  # verify=False para evitar SSL
        response.raise_for_status()
        print("  ✓ OK con requests")
        return response.json()
    except Exception as e:
        print(f"  ✗ requests falló: {type(e).__name__}: {e}")

    # Intento 2: curl
    try:
        print("  Intentando con curl...")
        resultado = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "60", "-k",
             "-H", "Accept: application/json",
             "-H", "User-Agent: Mozilla/5.0",
             url],
            capture_output=True, text=True, timeout=90
        )
        if resultado.returncode == 0 and resultado.stdout.strip():
            print("  ✓ OK con curl")
            return json.loads(resultado.stdout)
        else:
            print(f"  ✗ curl falló: return code {resultado.returncode}")
    except Exception as e:
        print(f"  ✗ curl falló: {type(e).__name__}: {e}")

    raise ConnectionError("No se pudo conectar con requests ni curl.")

def procesar_datos(datos_json):
    """Procesa datos JSON a DataFrame"""
    print("\n[T010] Procesando datos...")

    # Convertir JSON a DataFrame
    df_raw = pd.DataFrame(datos_json.get('ListaEESSPrecio', []))

    if df_raw.empty:
        raise ValueError("DataFrame vacío")

    print(f"  Columnas disponibles: {list(df_raw.columns)[:10]}...")

    # Mapear columnas JSON a nombres estándar
    mapeo_columnas = {
        'Rótulo': 'Gasolinera',
        'Provincia': 'Provincia',
        'Precio Gasoleo A': 'Precio_Diesel',
        'Precio Gasolina 95 E5': 'Precio_Gasolina_95',
        'Latitud': 'Latitud',
        'Longitud (WGS84)': 'Longitud',
        'IDEESS': 'ID_Estacion'
    }

    # Crear dataframe con columnas disponibles
    columnas_usar = {orig: nuevo for orig, nuevo in mapeo_columnas.items() if orig in df_raw.columns}
    df = df_raw[list(columnas_usar.keys())].rename(columns=columnas_usar)

    # Asegurar columnas mínimas
    for col in ['Gasolinera', 'Provincia', 'Latitud', 'Longitud', 'Precio_Gasolina_95', 'Precio_Diesel']:
        if col not in df.columns:
            if col == 'Gasolinera' and 'Rótulo' in df_raw.columns:
                df['Gasolinera'] = df_raw['Rótulo']
            else:
                df[col] = np.nan

    # Convertir a numéricos
    for col in ['Latitud', 'Longitud', 'Precio_Gasolina_95', 'Precio_Diesel']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')

    return df

def main():
    print("="*80)
    print("TEST LOCAL: Descarga y procesamiento de datos de Carburantes")
    print("="*80)

    url_api = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

    try:
        print(f"\nDescargando de: {url_api}")
        datos_json = descargar_datos_api(url_api)

        print(f"\n✓ JSON descargado")
        print(f"  Fecha: {datos_json.get('Fecha', 'N/A')}")
        print(f"  Estaciones: {len(datos_json.get('ListaEESSPrecio', [])):,}")

        # Procesar
        df = procesar_datos(datos_json)

        print(f"\n✓ DataFrame procesado: {df.shape[0]} filas × {df.shape[1]} columnas")
        print(f"\n  Columnas finales: {list(df.columns)}")
        print(f"\n  Tipos de datos:")
        print(f"    {df.dtypes.to_string()}")

        print(f"\n  Primeros 3 registros:")
        print(df.head(3).to_string())

        print(f"\n  Estadísticas de precios:")
        for col in ['Precio_Diesel', 'Precio_Gasolina_95']:
            if col in df.columns:
                print(f"    {col}: min={df[col].min():.2f}, max={df[col].max():.2f}, media={df[col].mean():.2f}")

        print(f"\n  Valores nulos:")
        nulos = df.isnull().sum()
        if nulos.sum() > 0:
            print(f"    {nulos[nulos > 0].to_string()}")
        else:
            print(f"    ✓ Sin valores nulos")

        print(f"\n✓ TEST EXITOSO")
        return True

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    import urllib3
    urllib3.disable_warnings()  # Suprimir SSL warnings

    success = main()
    sys.exit(0 if success else 1)
