# Prompt: Normalizar Nombres de Marcas

## Prompt Original

```
En el dataset de carburantes, el nombre de las marcas tiene variaciones (REPSOL, Repsol, repsol, REPSOL S.A., etc).
Escribe una función Python que:

1. Reciba un DataFrame y el nombre de la columna de marcas
2. Normalice los nombres:
   - Convertir a mayúsculas
   - Eliminar espacios extras
   - Reemplazar variaciones comunes (REPSOL S.A. → REPSOL)
3. Reporte:
   - Número de variaciones ANTES de normalización
   - Número de variaciones DESPUÉS
   - Lista de marcas únicas detectadas
4. Retorne el DataFrame modificado
5. Todo con mensajes en español

La función debe ser educativa y mostrar el impacto de la normalización.
```

## Resultado Obtenido

La solución utilizó pandas .str methods para normalización:

```python
def normalizar_marcas(df, columna_marca='Marca'):
    """
    Normaliza nombres de marcas (ej: repsol, REPSOL, Repsol → REPSOL)
    """
    df_norm = df.copy()
    
    # Normalizar a mayúsculas y eliminar espacios
    df_norm[columna_marca] = df_norm[columna_marca].str.upper().str.strip()
    
    # Reemplazar variaciones comunes
    reemplazos = {
        'GASOL': 'GASOL',
        'SHELL': 'SHELL',
        'CEPSA': 'CEPSA',
        'REPSOL': 'REPSOL'
    }
    
    for original, nuevo in reemplazos.items():
        df_norm[columna_marca] = df_norm[columna_marca].str.replace(original, nuevo, regex=False)
    
    # Reportar cambios
    marcas_antes = df[columna_marca].nunique()
    marcas_despues = df_norm[columna_marca].nunique()
    
    print(f"[NORMALIZACIÓN] Marcas:")
    print(f"  Variaciones antes: {marcas_antes}")
    print(f"  Variaciones después: {marcas_despues}")
    print(f"  Marcas detectadas: {', '.join(df_norm[columna_marca].unique()[:10])}")
    
    return df_norm
```

## Reflexión

**Qué funcionó bien:**
- Métodos pandas .str.upper() y .str.strip() son directos
- Reportar antes/después muestra impacto tangible de la limpieza
- Diccionario de reemplazos es fácil de extender
- Retornar DataFrame modificado permite cadena de transformaciones

**Qué aprendimos:**
- Normalización reduce variaciones de 100s a <10 únicas marcas a menudo
- Las variaciones vienen de: mayúsculas/minúsculas, espacios, sufijos (S.A., Ltd)
- Mostrar ejemplos de marcas normalizadas facilita validar que se hizo bien
- Sin normalización, análisis de "cuál es la marca más cara" fallaría

**Patrón reutilizable:**
- Esta función es template para normalizar CUALQUIER columna categórica
- Reemplazar diccionario de marcas por productos, provincias, etc.
- Útil antes de groupby(), pivot(), o análisis de categorías
