# Prompt: Visualizar Relación Ubicación Geográfica vs Precio

## Prompt Original

```
Necesito ver si hay correlación entre la ubicación geográfica (lat/long) y el precio del carburante.
Escribe código Python que:

1. Use coordenadas (latitud, longitud) como ejes X/Y
2. Use color para representar precio (cmap colormap)
3. Cree scatter plot mostrando distribución geográfica
4. Incluya barra de color (colorbar) con escala de precios
5. Etiquetas geográficas y de precio en español
6. Tamaño y alpha apropiados para ver patrones

La pregunta de negocio es: ¿La ubicación afecta el precio del carburante?
```

## Resultado Obtenido

La solución utilizó scatter plot con mapa de colores:

```python
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(df['longitud'], df['latitud'], c=df['precio'], 
 cmap='RdYlGn_r', s=30, alpha=0.6)
ax.set_title('Ubicación Geográfica vs Precio de Carburante', fontsize=14, fontweight='bold')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Precio (€/L)')
plt.tight_layout()
plt.show()
```

## Reflexión

**Qué funcionó bien:**
- Scatter plot es ideal para mostrar relación entre 3+ variables (long, lat, precio)
- Colormap 'RdYlGn_r' (inverso: rojo=caro, verde=barato) es intuitivo
- Parámetro alpha=0.6 permite ver densidad de puntos (sobreposición)
- Colorbar añade leyenda automática del rango de precios

**Qué aprendimos:**
- La geografía SÍ afecta precios: zonas rurales son más baratas, urbanas más caras
- Scatter plot revela clusters geográficos que groupby nunca mostraría
- El color rojo/verde permite reconocimiento visual rápido sin leer números
- Parámetro s=30 (tamaño) es pequeño para ~11k puntos (legible)

** PROBLEMA ENCONTRADO EN EJECUCIÓN REAL:**
- Scatter plot único mezcla península e islas - difícil distinguir patrones por región
- **Solución aplicada:** Separar visualmente península (● círculo) e islas (▲ triángulo) con marcadores distintos
```python
def clasificar_region(lon):
 return 'Península' if lon > -10 else 'Islas'

df['tipo_region'] = df['Longitud'].apply(clasificar_region)

for region, color, marker in [('Península', 'steelblue', 'o'), ('Islas', 'coral', '^')]:
 mask = df['tipo_region'] == region
 ax.scatter(df[mask]['Longitud'], df[mask]['Latitud'],
 c=df[mask]['Precio_Diesel'], cmap='RdYlGn_r',
 s=30, alpha=0.6, edgecolors='none', label=region, marker=marker)
```
- Usar marcadores (marker) para distinguir regiones es más efectivo que solo color
- Agregar leyenda (legend) es crítico cuando hay múltiples series

**Patrón reutilizable:**
- Aplicable a: ventas vs ubicación, temperatura vs elevación, salarios vs región, etc.
- Patrón: scatter(X, Y, c=Z, cmap=...) + marcadores por grupo = análisis multivariante geográfico
- Colormaps: RdYlGn para valores buenos/malos, viridis para continuos neutros
- **Regla:** Cuando hay múltiples grupos geográficos (península, islas, archipiélagos), usar marcadores diferentes para claridad
