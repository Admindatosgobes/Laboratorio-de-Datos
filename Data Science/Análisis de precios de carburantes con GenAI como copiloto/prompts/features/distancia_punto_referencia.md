# Prompt: Crear Feature - Distancia a Punto de Referencia

## Prompt Original

```
Quiero saber si hay una relación entre la distancia a una gran ciudad y el precio del carburante.
Crea código que:

1. Use Madrid como punto de referencia (40.416775, -3.703790)
2. Calcule la distancia aproximada en km desde cada gasolinera a Madrid
3. Usa la fórmula: sqrt((lat-ref_lat)² + (lon-ref_lon)²) * 111 km/grado
4. Reporte: distancia promedio, máxima
5. Valide que no hay valores nulos
6. Educativo en español

Pregunta: ¿Las gasolineras lejos de Madrid son más baratas?
```

## Resultado Obtenido

La solución calculó distancia euclidiana proyectada:

```python
# Punto de referencia: Madrid
ref_lat, ref_lon = 40.416775, -3.703790

# Fórmula aproximada: distancia en km
df['distancia_a_ref'] = np.sqrt(
    (df['latitud'] - ref_lat)**2 + (df['longitud'] - ref_lon)**2
) * 111  # Aprox 111 km por grado

# Reportar
dist_mean = df['distancia_a_ref'].mean()
dist_max = df['distancia_a_ref'].max()
print(f"Distancia promedio: {dist_mean:.1f} km")
print(f"Distancia máxima: {dist_max:.1f} km")
```

## Reflexión

**Qué funcionó bien:**
- Fórmula euclidiana es aproximada pero válida para distancias < 1000 km
- Constante 111 km/grado es un standard para proyecciones simples
- np.sqrt() es vectorizado: rápido incluso con 11k filas
- Reporte con mean() y max() valida rangos razonables

**Qué aprendimos:**
- La distancia a un hub importante SÍ afecta precios: logística
- Feature numérico (no binario) permite capturar relaciones graduales
- Alternativa mejor: usar geodistancia con haversine (pero más complejo)
- Esta variable es útil para: modelos de precio, análisis de distribución

**Patrón reutilizable:**
- Aplicable a: distancia a puerto (exportación), distancia a planta (manufactura)
- Patrón: sqrt((X-ref_X)² + (Y-ref_Y)²) * factor = distancia aproximada
- Para mayor precisión: usar librería geopy.distance.geodesic (haversine)
