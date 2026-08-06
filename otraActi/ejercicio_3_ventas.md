# Ejercicio 3 — Ventas
Dataset: `3_ventas.csv`

**Contexto:** Eres el/la analista comercial. El gerente de ventas
necesita el reporte de comisiones y desempeño del último periodo, pero
el archivo viene del CRM con errores típicos de digitación y de
exportación.

---

## Preguntas de negocio

1. El gerente pide primero un chequeo de calidad: ¿cuántos pedidos
   están duplicados por un error de sincronización del CRM? Elimínalos.

   R/ Realizando el respectivo analizis sobre la base de datos para identificar la duplicidad de los registros, se detectaron 2 pedidos duplicados debido a un posible error de sincronizacion del CRM por ende se procedió a su debida eliminacion y se conservó una única instancia de cada uno de estos registros manteniendo la integridad de los datos.

2. El mismo vendedor aparece registrado de formas distintas ("María
   Gómez", "maria gómez"). Unifica los nombres para que las comisiones
   se calculen correctamente por persona y no se dividan entre "dos
   vendedores" que en realidad son el mismo.

   R/ Se identificó una inconsistencia en la forma en que se registraban los nombres de los vendedores. Para garantizar la integridad y confiabilidad del análisis, se estandarizaron los registros bajo un formato único, asegurando que todas las ventas quedaran correctamente asociadas a su respectivo vendedor y poder realizar el calculo preciso de sus comisiones.

3. Se detectó un pedido con cantidad negativa, lo cual no es posible en
   una venta real (fue un error de digitación al capturar el pedido).
   Encuéntralo y corrígelo.

   R/ Durante el proceso de validación de la calidad de los datos se identificó un registro de venta con una cantidad negativa, un valor no válido para este tipo de transacciones y atribuible a un error de digitación. Para corregir esta inconsistencia, se ajustó el registro reemplazando el valor negativo por su correspondiente valor positivo, garantizando así la consistencia e integridad de la información, así como la precisión de los cálculos y análisis posteriores.

4. Hay pedidos sin precio unitario registrado. Como no podemos dejarlos
   en cero (subestimaría las ventas), rellénalos con el precio promedio
   de ese mismo producto.

   R/ Listo

5. Hay pedidos sin vendedor o sin región asignada; como no se pueden
   atribuir a nadie para el cálculo de comisiones, elimínalos del
   análisis.

   R/

6. Calcula el `monto_bruto` de cada pedido (`cantidad * precio_unitario`)
   y el `monto_neto` aplicando el descuento (`descuento_pct`).

   R/ 


7. **Pregunta del gerente:** "¿Quién es el mejor vendedor del periodo?"
   Calcula el total de `monto_neto` vendido por cada vendedor y el
   número de pedidos que hizo. Ordena de mayor a menor.

8. Recursos Humanos va a pagar comisión del 5% sobre el monto neto
   vendido por cada vendedor. Calcula cuánto le corresponde a cada uno.

9. **Pregunta del gerente:** "¿Qué región está vendiendo más y qué
   producto es el más fuerte en cada región?" Construye una tabla
   dinámica de `monto_neto` por región y producto.

10. El gerente sospecha que se están dando demasiados descuentos.
    Calcula qué porcentaje de los pedidos tuvo descuento mayor a 0 y
    cuánto dinero total "se perdió" en descuentos (`monto_bruto -
    monto_neto`).

---
*Tip: usa `df['vendedor'].unique()` para confirmar que ya no queden
nombres duplicados por formato antes de calcular comisiones.*