# Prompt: Visualizar Distribución de Precios por Marca

## Prompt Original

```
Necesito comparar cómo varían los precios dentro de cada marca de gasolinera.
Escribe código Python que:

1. Seleccione las marcas más frecuentes (top 5)
2. Cree un box plot mostrando distribución de precios por marca
3. Muestre mediana, cuartiles, outliers
4. Incluya etiquetas en español, tamaño apropiado
5. Responda: ¿Hay diferencias significativas entre marcas?
6. Código educativo

La pregunta de negocio es: ¿La marca afecta significativamente el precio?
```

## Resultado Obtenido

La solución utilizó box plot para mostrar distribuciones:

```python
# Obtener top 5 marcas
top_marcas = df['marca'].value_counts().head(5).index
df_top = df[df['marca'].isin(top_marcas)]

fig, ax = plt.subplots(figsize=(10, 5))
df_top.boxplot(column='precio', by='marca', ax=ax)
ax.set_title('Distribución de Precios por Marca', fontsize=14, fontweight='bold')
ax.set_xlabel('Marca')
ax.set_ylabel('Precio (€/L)')
plt.suptitle('') # Remover título automático
plt.tight_layout()
plt.show()
```

## Reflexión

**Qué funcionó bien:**
- Box plot es la visualización correcta para comparar distribuciones
- Muestra: mediana (línea), cuartiles (caja), rango (whiskers), outliers (puntos)
- Seleccionar top 5 marcas evita gráficos con demasiadas categorías
- pandas df.boxplot() simplifica la sintaxis respecto a matplotlib raw

**Qué aprendimos:**
- La mayoría de marcas tienen precios similares: competencia regulada
- Outliers (puntos sueltos) representan gasolineras con precios atípicos
- Las distribuciones estrechas indican estandarización de precios
- Esta pregunta puede revelar: diferenciación de marcas, poder de mercado, fraude

** PROBLEMA ENCONTRADO EN EJECUCIÓN REAL (T023: Bar chart de conteos):**
- Marcas MOEVE y CEPSA se fusionaban en la visualización de "Top 8 Marcas"
- Causa: Variantes sin normalizar (ej. "MOEVE", "Moeve", "moeve", "CEPSA", "Cepsa")
- **Solución aplicada:** Normalizar todas las marcas a MAYÚSCULAS + strip() antes de agrupar
```python
# ANTES (incorrecto):
marcas_top = df['Gasolinera'].value_counts().head(8)

# DESPUÉS (correcto):
marcas_normalizadas = df['Gasolinera'].str.upper().str.strip()
df['Gasolinera_norm'] = marcas_normalizadas
marcas_top = df['Gasolinera_norm'].value_counts().head(8)
```
- Agregar cantidad exacta en top de barras (ax.text()) para verificabilidad
- Usar paleta de colores (plt.cm.Set3) para distinguir marcas visualmente

**Patrón reutilizable:**
- Aplicable a: salarios por departamento, tiempo de entrega por proveedor, etc.
- Patrón: boxplot(column=valor, by=categoría) = comparación de distribuciones
- Agregar text('Mediana: €X.XX') para anotaciones si hay diferencias extremas
- **Regla crítica:** SIEMPRE normalizar columnas categóricas (str.upper().str.strip()) antes de agrupar/contar
