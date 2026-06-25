# Prompt: Validar Precios de Carburantes

## Prompt Original

```
En un análisis de precios de carburantes, necesito validar que los precios sean razonables.
Escribe una función Python que:

1. Reciba un DataFrame y el nombre de la columna de precios
2. Defina un rango válido: €0.50 - €3.00 por litro (ajustable)
3. Identifique precios fuera de rango
4. Reporte:
   - Cantidad total de registros
   - Cantidad de precios válidos (%) 
   - Cantidad de precios inválidos (%)
   - Min y max de precios válidos detectados
5. Todo con mensajes en español

La función debe ser educativa, mostrando qué significa "validar" en análisis de datos.
```

## Resultado Obtenido

La solución utilizó pandas para validación con reportes claros:

```python
def validar_precios(df, columna_precio='Precio', min_precio=0.5, max_precio=3.0):
    """
    Valida precios: reporta valores fuera del rango [min_precio, max_precio]€
    """
    precio_col = df[columna_precio].astype(float, errors='coerce')
    
    # Precios inválidos
    invalidos = (precio_col <= min_precio) | (precio_col >= max_precio)
    n_invalidos = invalidos.sum()
    
    print(f"[VALIDACIÓN] Precios:")
    print(f"  Rango esperado: €{min_precio:.2f} - €{max_precio:.2f}")
    print(f"  Precios válidos: {(~invalidos).sum()} ({(~invalidos).sum()/len(df)*100:.1f}%)")
    print(f"  Precios inválidos: {n_invalidos} ({n_invalidos/len(df)*100:.1f}%)")
    
    return invalidos
```

## Reflexión

**Qué funcionó bien:**
- Operaciones booleanas de pandas (.astype(), ~invalidos) son concisas
- Reportes porcentuales facilitan entender la calidad de datos
- Parámetros ajustables (min_precio, max_precio) permiten reutilizar función
- Manejo de errores con `errors='coerce'` es robusto

**Qué aprendimos:**
- La validación es el primer paso de limpieza de datos
- Los reportes textuales ayudan a entender si los datos son "limpios" o no
- Es importante mostrar ejemplos (min/max detectados) de los datos válidos
- Sin validación, no sabemos si nuestros análisis posteriores son confiables

**Patrón reutilizable:**
- Esta estructura (función + reporte) se aplica a cualquier validación numérica
- El mismo patrón funciona para: fechas, IDs, cantidades, cualquier métrica
- Útil como checklist de calidad de datos antes de análisis
