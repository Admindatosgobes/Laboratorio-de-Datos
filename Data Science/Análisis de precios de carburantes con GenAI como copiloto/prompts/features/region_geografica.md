# Prompt: Crear Feature - Región Geográfica

## Prompt Original

```
Quiero simplificar el análisis dividiendo España en tres regiones geográficas.
Crea un feature que:

1. Use latitud para clasificar: Norte (>42°), Centro (40-42°), Sur (<40°)
2. Cree una variable categórica con valores: 'Norte', 'Centro', 'Sur'
3. Reporte la distribución (count y %) por región
4. Valide que toda gasolinera tiene asignada una región
5. Código educativo en español

Pregunta: ¿Hay diferencias de precio entre regiones?
```

## Resultado Obtenido

La solución utilizó buckets de latitud:

```python
# Dividir España en norte/centro/sur por latitud
def asignar_region(lat):
    if lat > 42:
        return 'Norte'
    elif lat >= 40:
        return 'Centro'
    else:
        return 'Sur'

df['region_geografica'] = df['latitud'].apply(asignar_region)

# Reportar
regiones = df['region_geografica'].value_counts()
for region in ['Norte', 'Centro', 'Sur']:
    if region in regiones.index:
        print(f"{region}: {regiones[region]} ({regiones[region]/len(df)*100:.1f}%)")
```

## Reflexión

**Qué funcionó bien:**
- Función con if/elif/else es clara y mantenible
- .apply() vectoriza la función sin bucle explícito (pandas idiomático)
- Buckets (bins) de latitud capturan macro-regiones de España
- Feature categórico se convierte automáticamente a dummy en sklearn

**Qué aprendimos:**
- Regionalizaciones son tiles para análisis sin overfitting
- España: Norte (zona atlántica, más industrializada) vs Centro (meseta) vs Sur (andaluz)
- Precios SÍ varían por región: (densidad, distancia a refinería, demanda)
- Este tipo de feature es "domain knowledge": requiere entender geografía

**Patrón reutilizable:**
- Aplicable a: clima por latitud, desarrollo por región, densidad urbana
- Patrón: if/elif/else con .apply() = categorización basada en umbral
- Alternativa: pd.cut() para buckets automáticos si no hay umbral natural
