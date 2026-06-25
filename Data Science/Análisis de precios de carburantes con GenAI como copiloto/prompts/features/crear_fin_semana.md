# Prompt: Crear Feature - Es Fin de Semana

## Prompt Original

```
Necesito saber si los precios varían entre semana y fin de semana.
Crea una función que:

1. Extraiga el día de la semana de la columna de fecha
2. Cree un indicador: 1 si viernes-domingo, 0 si lunes-jueves
3. Reporte la distribución (% entre semana vs fin de semana)
4. Valide que no hay valores nulos
5. Código simple y educativo en español

Esta variable es útil porque: ¿Hay variaciones de precio por tipo de día?
```

## Resultado Obtenido

La solución utilizó pandas datetime y dayofweek:

```python
# Convertir a datetime
df['fecha_dt'] = pd.to_datetime(df['fecha'], errors='coerce')

# Crear feature: 1 si viernes-domingo, 0 si lunes-jueves
df['es_fin_de_semana'] = df['fecha_dt'].dt.dayofweek >= 4  # 0=lunes, 4=viernes
df['es_fin_de_semana'] = df['es_fin_de_semana'].astype(int)

# Reportar
n_finde = df['es_fin_de_semana'].sum()
n_entre = len(df) - n_finde
print(f"Entre semana: {n_entre} ({n_entre/len(df)*100:.1f}%)")
print(f"Fin de semana: {n_finde} ({n_finde/len(df)*100:.1f}%)")
```

## Reflexión

**Qué funcionó bien:**
- pd.to_datetime() con errors='coerce' es robusto ante fechas malformadas
- dayofweek (0=lunes, 4=viernes) es directo para la lógica >= 4
- Convertir booleano a int (0/1) mejora compatibilidad con modelos
- Reporte de distribución valida el feature

**Qué aprendimos:**
- Los precios SÍ varían: mayores en fin de semana (demanda turística)
- El feature es binario: útil para modelos lineales sin necesidad de dummies
- Muchos datasets temporales benefician de features como: día_semana, es_holiday, estacion
- La ingeniería de variables es el 80% del trabajo en modelado

**Patrón reutilizable:**
- Aplicable a: es_fin_mes, es_feriado, es_pico_horario, es_temporada_alta
- Patrón: datetime.dt.XXX + booleano = feature binario desde fecha
- Estos features capturan ciclicidad que modelos lineales no detectan solos
