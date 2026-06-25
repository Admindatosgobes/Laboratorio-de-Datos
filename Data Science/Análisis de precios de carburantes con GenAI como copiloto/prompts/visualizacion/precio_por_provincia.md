# Prompt: Visualizar Precio Promedio por Provincia

## Prompt Original

```
Necesito un gráfico que muestre cuál es la provincia más cara para carburante.
Escribe código Python que:

1. Agrupe precios por provincia
2. Calcule el precio promedio por provincia
3. Ordene de mayor a menor precio
4. Cree un gráfico de barras (bar plot) con matplotlib
5. Incluya título, etiquetas en español, tamaño apropiado
6. Todo de manera educativa

La pregunta de negocio es: ¿Qué provincia tiene los carburantes más caros?
```

## Resultado Obtenido

La solución utilizó groupby + plot para crear visualización clara:

```python
# Agrupar por provincia
precio_prov = df.groupby('provincia')['precio'].mean().sort_values(ascending=False)

# Crear figura
fig, ax = plt.subplots(figsize=(12, 5))
precio_prov.plot(kind='bar', ax=ax, color='steelblue')
ax.set_title('Precio Promedio de Carburante por Provincia', fontsize=14, fontweight='bold')
ax.set_xlabel('Provincia')
ax.set_ylabel('Precio (€/L)')
ax.tick_params(axis='x', rotation=90)
plt.tight_layout()
plt.show()
```

## Reflexión

**Qué funcionó bien:**
- pandas groupby().mean() es conciso para agregación
- sort_values(ascending=False) ordena de mayor a menor
- matplotlib bar chart es clara y legible
- Parámetro figsize=(12, 5) adapta visualización para muchas provincias

**Qué aprendimos:**
- Ordenar de mayor a menor mejora la respuesta a la pregunta "¿cuál es el más caro?"
- Rotación de etiquetas (rotation=90) es necesaria para ~50 provincias
- Colores consistentes ayudan a la lectura profesional
- Esta es una pregunta de negocio típica: identificar mercados con mayores precios

** PROBLEMA ENCONTRADO EN EJECUCIÓN REAL:**
- Los valores de precio por provincia son muy similares (1.40-1.55€) y sin ajuste de eje X no se ve diferencia
- **Solución aplicada:** Escalar dinámicamente eje X basado en min/max de datos
```python
precio_prov = df.groupby('Provincia')['Precio_Diesel'].mean().sort_values(ascending=False)
precio_prov.plot(kind='barh', ax=ax, color='steelblue')
ax.set_xlim(precio_prov.min() * 0.95, precio_prov.max() * 1.05) # NUEVO
```
- Usar gráfico horizontal (barh) en lugar de vertical (bar) también ayuda cuando las provincias son muchas

**Patrón reutilizable:**
- Aplicable a cualquier "promedio por categoría" (ventas por región, peso por especie, etc.)
- El patrón es: groupby + plot + dynamic scaling = respuesta visual clara
- **Regla:** Siempre escalar ejes cuando los valores varían poco (< 10% de diferencia)
