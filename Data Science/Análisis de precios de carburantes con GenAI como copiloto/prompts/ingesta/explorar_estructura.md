# Prompt: Explorar Estructura del Dataset

## Prompt Original

```
Una vez descargado el dataset de carburantes, necesito explorar su estructura.
Escribe código Python que:

1. Muestre el nombre y tipo de datos de cada columna (.info())
2. Muestre los primeros 5 registros (.head())
3. Muestre estadísticas básicas (.describe())
4. Reporte el número total de filas y columnas
5. Identifique columnas con valores nulos
6. Todo con comentarios en español

El código debe ser educativo, mostrando qué información aporta cada exploración.
```

## Resultado Obtenido

La solución utilizó métodos pandas estándar pero educativos:

```python
# Exploración de estructura
print(f"Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")
print("\nTipos de datos:")
print(df.info())

print("\nPrimeros registros:")
print(df.head(5))

print("\nEstadísticas numéricas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())
```

## Reflexión

**Qué funcionó bien:**
- Métodos pandas estándar (.info(), .head(), .describe()) son eficientes
- Orden lógico de exploración: estructura → muestras → estadísticas → calidad
- Útil para entender qué limpieza se necesitará

**Qué aprendimos:**
- La exploración inicial es crítica para entender datos antes de procesar
- GenAI sugiere orden lógico sin pedirlo explícitamente
- Los métodos pandas son suficientes, no hay necesidad de librerías adicionales

**Patrón reutilizable:**
- Esta estructura de exploración puede aplicarse a cualquier CSV
- Útil como checklist visual antes de limpieza
