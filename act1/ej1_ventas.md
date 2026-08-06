# Ejercicio 1 — Ventas (Negocio: TiendaMax, Retail/Electrónica)

**Archivo:** `ventas_desnormalizado.csv`

**Contexto:** TiendaMax es una cadena de tiendas de electrónica y mobiliario de oficina con varias
sucursales. Este CSV es una exportación cruda del sistema de ventas: cada fila es una venta, pero
los datos de cliente, producto y sucursal vienen repetidos y con inconsistencias (nombres de
sucursal con mayúsculas/espacios distintos, fechas en 3 formatos diferentes, método de pago sin
normalizar, nulos y una fila duplicada).

## Flujo de trabajo
1. Leer el CSV con pandas.
2. Explorar y limpiar: nulos, duplicados, inconsistencias de texto, formatos de fecha mixtos, tipos de datos.
3. **Normalizar** en tablas relacionadas (3FN): `clientes`, `productos`, `sucursales`, `ventas` (con FKs).
4. Conectarse a PostgreSQL y cargar las tablas normalizadas:
```python
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://usuario:password@localhost:5432/tiendamax")
clientes.to_sql("clientes", engine, if_exists="replace", index=False)
```
5. Responder las preguntas con pandas o `pd.read_sql()`.
6. Generar el gráfico final.

## Preguntas
1. ¿Cuáles son las 3 sucursales con mayor ingreso total después de aplicar los descuentos? (cuidado con los nombres de sucursal mal escritos/con espacios extra).
2. ¿Qué vendedor tiene el ticket promedio más alto, y cómo cambia el resultado si excluyes las ventas con descuento ≥ 10%?
3. ¿Cuál es el producto con mayor ingreso total y cuál con mayor cantidad vendida? ¿Son el mismo producto? Explica por qué podrían diferir.
4. ¿Qué porcentaje de las ventas de clientes "Empresarial" se pagó por transferencia vs. clientes "Individual"? (normaliza los valores de `metodo_pago` antes de comparar).
5. Después de eliminar duplicados y nulos en `total_venta`, calcula el ingreso mensual y determina si hay una tendencia creciente o decreciente en el año.

## Gráfico final
**Usar matplotlib** (`matplotlib.pyplot`) con `plt.subplots(2, 2, figsize=(14, 10))` para armar un
dashboard de 4 paneles: ingreso por sucursal, ingreso mensual (línea de tendencia), top 5 productos
por ingreso, y ticket promedio por vendedor.

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes[0,0].bar(...)   # ingreso por sucursal
axes[0,1].plot(...)  # ingreso mensual
axes[1,0].barh(...)  # top 5 productos
axes[1,1].bar(...)   # ticket promedio por vendedor
plt.tight_layout()
plt.savefig("ej1_dashboard.png", dpi=150)
plt.show()
```

## Checklist de dificultad
- [ ] Manejo de fechas en múltiples formatos.
- [ ] Normalización de texto (`.str.strip()`, `.str.lower()`, mapeos de valores equivalentes).
- [ ] Eliminación de duplicados exactos.
- [ ] Manejo de nulos con criterio (imputar vs. eliminar, justificado).
- [ ] Diseño de esquema normalizado (3FN) antes de cargar a PostgreSQL.
- [ ] Carga con `to_sql()` y validación con `pd.read_sql()`.
- [ ] Gráfico compuesto que sintetice el análisis.
