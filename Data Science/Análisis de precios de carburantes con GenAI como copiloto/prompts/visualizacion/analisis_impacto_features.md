# Prompt: Análisis de Impacto de Features en Precios

## Contexto
Después de crear 3 nuevas variables (es_fin_semana, distancia_a_madrid, region), necesitamos visualizar cómo cada una impacta el precio. Sin datos históricos, modelado predictivo no es realista; mejor mostrar correlaciones y patrones.

## Prompt Original

"Crea 3 visualizaciones Plotly que muestren cómo cada feature engineered impacta el precio del carburante:

1. **Scatter plot precio vs distancia a Madrid** - con línea de tendencia polinomial para ver si hay correlación geográfica
2. **Box plot comparativo fin_semana vs entre_semana** - comparar precios medio/mediana entre ambos grupos
3. **Box plot por región** (norte/centro/sur) - ver si hay diferencias regionales significativas

Cada visualización debe:
- Ser interactiva (Plotly)
- Tener título que responda una pregunta de negocio
- Incluir estadísticas en la consola (media, conteos, correlación)
- Ser interpretable por no-técnicos"

## Resultado Obtenido

### T034: Scatter plot Precio vs Distancia a Madrid
```python
fig_t34 = px.scatter(
 df,
 x='distancia_a_madrid',
 y='Precio_Diesel',
 color='Precio_Diesel',
 color_continuous_scale='RdYlGn_r',
 opacity=0.5
)

# Calcular correlación
corr_distancia = df['distancia_a_madrid'].corr(df['Precio_Diesel'])

# Añadir línea de tendencia (polinomio grado 1)
z = np.polyfit(df['distancia_a_madrid'].dropna(), 
 df.loc[df['distancia_a_madrid'].notna(), 'Precio_Diesel'], 1)
p = np.poly1d(z)
x_trend = np.linspace(df['distancia_a_madrid'].min(), max, 100)
y_trend = p(x_trend)

fig_t34.add_scatter(x=x_trend, y=y_trend, mode='lines', 
 line=dict(color='red', width=2, dash='dash'))
```

**Output**: Muestra visualmente si Madrid es "hub" o no en precios.
- Si correlación ≈ 0: distancia NO es determinante
- Si correlación > 0: precios SUBEN alejándose (provincias caras lejos)
- Si correlación < 0: precios BAJAN alejándose (Madrid es más caro)

### T035: Box Plot Fin de Semana vs Entre Semana
```python
# Calcular diferencia de medias
precio_semana = df[df['es_fin_semana'] == 0]['Precio_Diesel'].mean()
precio_fin = df[df['es_fin_semana'] == 1]['Precio_Diesel'].mean()
diferencia = precio_fin - precio_semana

# Box plot comparativo
df_temp['tipo_dia'] = df_temp['es_fin_semana'].map({0: 'Entre semana', 1: 'Fin de semana'})
fig_t35 = px.box(df_temp, x='tipo_dia', y='Precio_Diesel', color='tipo_dia', points='outliers')
```

**Output**: Responde "¿Es más caro llenar en fin de semana?"
- Diferencia < €0.01: NO hay efecto temporal
- Diferencia > €0: Fin de semana MÁS CARO
- Diferencia < €0: Fin de semana MÁS BARATO

### T036: Box Plot por Región
```python
# Estadísticas por región
for region in ['Norte', 'Centro', 'Sur']:
 precio_region = df[df['region'] == region]['Precio_Diesel'].mean()
 count = len(df[df['region'] == region])
 print(f"{region}: €{precio_region:.3f} ({count} estaciones)")

# Box plot con categorías ordenadas
fig_t36 = px.box(df, x='region', y='Precio_Diesel', color='region',
 category_orders={'region': ['Norte', 'Centro', 'Sur']})
```

**Output**: Identifica la región más cara/barata
- Diferencia < €0.05: regiones homogéneas en precio
- Diferencia > €0.05: fragmentación regional significativa

### T037: Interpretación en Lenguaje de Negocio
```python
print(f" CONCLUSIONES:")
print(f"1. DISTANCIA A MADRID (corr={corr_distancia:.3f})")
if abs(corr_distancia) < 0.1:
 print(f" ⇒ Madrid NO es determinante en precios")
else:
 print(f" ⇒ Distancia geográfica SÍ impacta")

print(f"2. FIN DE SEMANA (diferencia=€{diferencia:+.3f})")
if abs(diferencia) < 0.01:
 print(f" ⇒ Sin efecto temporal")
else:
 print(f" ⇒ El fin de semana {'más caro' if diferencia > 0 else 'más barato'}")

print(f"3. REGIÓN")
max_region = df.groupby('region')['Precio_Diesel'].mean().idxmax()
print(f" ⇒ {max_region} es la más cara")
```

## Reflexión

### ¿Por qué funcionó este enfoque?

1. **Sin datos históricos → Sin predicciones ficticias**
 - Dataset es "snapshot" de un día, no serie temporal
 - Modelado predictivo requeriría histórico de 30+ días
 - Decisión: mostrar patrones reales en los datos presentes

2. **Cada visualización responde una pregunta clara**
 - T034: "¿Hay un hub económico?" (geografía)
 - T035: "¿Varía por temporalidad?" (fin de semana)
 - T036: "¿Hay fragmentación regional?" (región)
 - No es "predicción ficta", es "análisis de datos reales"

3. **Métrica de éxito: correlación observable**
 - Línea de tendencia = patrón visual inmediato
 - Diferencia de medias = respuesta en €
 - Box plot = distribución y outliers visibles
 - Mejor que RMSE/R² que no tienen contexto sin histórico

### Patrón Reutilizable: "Feature Impact Analysis"

Para cualquier dataset nuevo:
1. Después de feature engineering, NO saltaras a modelado
2. Primero, visualiza cada feature vs target
3. Calcula correlaciones simples (Pearson)
4. Usa box plots para grupos categóricos (region, type_day)
5. Interpreta en términos de negocio (€, porcentajes, estadísticas)
6. Recién entonces decide si modelado tiene sentido

**Aplicaciones:**
- Datasets de marketing: feature impact en conversion
- Datasets médicos: feature impact en diagnóstico
- Datasets de logística: feature impact en entrega tardía
- Datasets financieros: feature impact en riesgo de crédito

### Lección: Simplicidad Pedagógica

Preferir:
- Scatter + trendline (interpretable visualmente)
- Box plot (mediana, cuartiles claros)
- Diferencia de medias en €/contexto del negocio

Evitar:
- Modelos complejos sin histórico (overfitting guaranteed)
- Métricas técnicas sin interpretación (R² = ???)
- Predicciones "mágicas" sin base real
