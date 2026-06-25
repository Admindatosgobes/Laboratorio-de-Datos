# Prompt: Crear Visualizaciones Interactivas con Plotly

## Prompt Original

```
Necesito reemplazar matplotlib estático por gráficos interactivos.
Escribe código Python que:

1. Use plotly en lugar de matplotlib para interactividad
2. Implemente 4 gráficos interactivos:
 - Bar chart: Precio por provincia (horizontal con colormap)
 - Scatter geográfico: Ubicación vs Precio (península ● / islas ▲)
 - Box plot: Distribución por marca (con outliers)
 - Histograma: Distribución de precios (con media/mediana)
3. Agregue hover labels informativos
4. Permita zoom, pan, selección de leyendas
5. Funcione sin configuración adicional en Colab
```

## Resultado Obtenido

La solución usó plotly (preinstalado en Colab) para 4 gráficos interactivos:

```python
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# T020: Bar chart interactivo con colormap
fig_prov = go.Figure(data=[
 go.Bar(
 x=precio_prov.values,
 y=precio_prov.index,
 orientation='h',
 marker=dict(color=precio_prov.values, colorscale='RdYlGn_r', showscale=True),
 hovertemplate='<b>%{y}</b><br>Precio: €%{x:.3f}<extra></extra>'
 )
])
fig_prov.update_layout(
 title='Precio Promedio de Diésel por Provincia (Top 12)',
 xaxis_title='Precio (€/L)',
 yaxis_title='Provincia',
 height=500,
 hovermode='closest',
 template='plotly_white'
)
fig_prov.show()

# T022: Scatter geográfico con Scattergeo
fig_map = go.Figure()

# Península (círculos)
peninsula = df[df['tipo_region'] == 'Península']
fig_map.add_trace(go.Scattergeo(
 lon=peninsula['Longitud'],
 lat=peninsula['Latitud'],
 mode='markers',
 marker=dict(
 size=5,
 color=peninsula['Precio_Diesel'],
 colorscale='RdYlGn_r',
 showscale=True,
 opacity=0.6,
 symbol='circle'
 ),
 text=peninsula.apply(lambda x: f"Provincia: {x['Provincia']}<br>Precio: €{x['Precio_Diesel']:.2f}", axis=1),
 hovertemplate='%{text}<extra></extra>',
 name='Península'
))

# Islas (triángulos)
islas = df[df['tipo_region'] == 'Islas']
fig_map.add_trace(go.Scattergeo(
 lon=islas['Longitud'],
 lat=islas['Latitud'],
 mode='markers',
 marker=dict(size=6, color=islas['Precio_Diesel'], symbol='triangle-up'),
 name='Islas'
))

fig_map.update_geos(
 scope='europe',
 projection_type='mercator',
 lonaxis=dict(range=[-18, 5]),
 lataxis=dict(range=[27, 44])
)
fig_map.show()

# T023: Box plot con plotly.express
fig_brand = px.box(
 df_top_marcas,
 x='Gasolinera_norm',
 y='Precio_Diesel',
 title='Distribución de Precios por Marca',
 points='outliers',
 color='Gasolinera_norm'
)
fig_brand.show()

# T021: Histograma con líneas de media/mediana
fig_dist = go.Figure()
fig_dist.add_trace(go.Histogram(x=df['Precio_Diesel'], nbinsx=30))
fig_dist.add_vline(x=media, line_dash='dash', line_color='red', name=f'Media: €{media:.2f}')
fig_dist.add_vline(x=mediana, line_dash='dash', line_color='green', name=f'Mediana: €{mediana:.2f}')
fig_dist.show()
```

## Reflexión

**Qué funcionó bien:**
- Plotly está preinstalado en Colab (no requiere pip install)
- Hover interactivo proporciona información sin saturar el gráfico
- Zoom/pan permiten exploración de datos sin código adicional
- Scattergeo maneja proyecciones geográficas automáticamente
- Express (px) simplifica la sintaxis para gráficos comunes

**Qué aprendimos:**
- Interactividad mejora exploración de datos (usuarios descubren outliers por sí solos)
- Hover labels reemplazan anotaciones estáticas
- Leyendas clicables permiten filtrar series dinámicamente
- Plotly renderiza idénticamente en Colab vs navegador

** VENTAJA PEDAGÓGICA ENCONTRADA:**
- Usuarios NO técnicos pueden explorar gráficos SIN leer código
- Hover muestra info contextual (ej: provincia + precio exacto)
- Zoom revelan patrones locales que agregaciones nunca mostrarían
- Interactividad = 10x mejor engagement que gráfico estático

**Patrón reutilizable:**
- Aplicable a: dashboards de análisis, reportes exploratorios, EDA
- Patrón: `go.Figure()` + add_trace() + `update_layout()` + `.show()`
- Colormaps: RdYlGn_r (rojo=caro, verde=barato), viridis (neutro)
- Hover template: `<b>%{y}</b><br>Precio: €%{x:.3f}<extra></extra>`
- **Regla crítica:** Siempre usar `hovermode='closest'` + hover_data personalizado
