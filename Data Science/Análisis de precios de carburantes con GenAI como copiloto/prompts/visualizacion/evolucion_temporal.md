# Prompt: Visualizar Evolución Temporal de Precios

## Prompt Original

```
Necesito ver cómo evolucionan los precios de carburante a lo largo del tiempo.
Escribe código Python que:

1. Ordene datos por fecha
2. Agrupe por fecha (o período) y calcule precio promedio
3. Cree un gráfico de líneas (line plot) mostrando la tendencia
4. Incluya grid para facilitar lectura
5. Etiquetas en español, tamaño apropiado
6. Código educativo

La pregunta de negocio es: ¿Hay tendencia al alza o a la baja en los precios?
```

## Resultado Obtenido

La solución utilizó line plot con tendencia clara:

```python
# Ordenar por fecha
df_sorted = df.sort_values('fecha')
precio_evolve = df_sorted.groupby('fecha')['precio'].mean()

fig, ax = plt.subplots(figsize=(12, 5))
precio_evolve.plot(ax=ax, color='green', linewidth=2)
ax.set_title('Evolución Temporal de Precios de Carburante', fontsize=14, fontweight='bold')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio Promedio (€/L)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Reflexión

**Qué funcionó bien:**
- Line plot (color verde, linewidth=2) es la elección natural para series temporales
- grid(True, alpha=0.3) facilita lectura sin sobrecargar
- groupby + plot permite ver tendencias en vez de puntos individuales
- Ordenar por fecha (sort_values) es crítico antes de agrupar

**Qué aprendimos:**
- Las series temporales requieren ordenamiento: sort_values('fecha') es obligatorio
- Agregar grid facilita la interpretación de valores
- Lineas gruesas (linewidth=2) mejoran visibilidad en proyecciones
- Esta pregunta revela ciclos económicos: vacaciones, cambios geopolíticos, estacionalidad

**Patrón reutilizable:**
- Aplicable a cualquier serie temporal: ventas, temperatura, tráfico, etc.
- Patrón: sort_values() + groupby() + line plot = análisis de tendencia
- Agregación por período (día, mes, trimestre) suaviza ruido
