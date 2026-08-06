--- ¿Cuáles son las 3 sucursales con mayor ingreso total después de aplicar los descuentos? (cuidado con los nombres de sucursal mal escritos/con espacios extra).
SELECT sucursal, SUM(total_venta - (total_venta * descuento_pct)) precio_final
FROM ventas
         inner join public.sucursal s on s.id_sucursal = ventas.id_sucursal
group by sucursal
order by precio_final DESC
limit 3;

--- ¿Qué vendedor tiene el ticket promedio más alto, y cómo cambia el resultado si excluyes las ventas con descuento ≥ 10%?

-- Con descuento
select vendedor, avg(total_venta - (total_venta * descuento_pct)) precio_final
from ventas
         inner join vendedor v on v.id_vendedor = ventas.id_vendedor
group by vendedor
order by precio_final DESC
limit 1;

-- Sin descuento
select vendedor, avg(total_venta - (total_venta * descuento_pct)) promedio_precio_final
from ventas
         inner join vendedor v on v.id_vendedor = ventas.id_vendedor
where descuento_pct < 0.1
group by vendedor
order by promedio_precio_final DESC
limit 1;

select *, total_venta - (total_venta * descuento_pct) promedio_precio_final from ventas;




---¿Cuál es el producto con mayor ingreso total y cuál con mayor cantidad vendida? ¿Son el mismo producto? Explica por qué podrían diferir.
-- Mayores cantidades vendidas
select producto, cantidad from ventas
inner join public.producto p on p.id_producto = ventas.id_producto
group by producto, cantidad
order by cantidad DESC;

-- Producto de mayor ingreso
select producto, SUM(total_venta - (total_venta * descuento_pct)) precio_final
from ventas
    inner join producto p on p.id_producto = ventas.id_producto
group by producto
order by precio_final DESC
limit 1;
------ No son el mismo producto, y esto sucede porque el precio del producto con mas ganancia es mucho mayor al mas vendido

---¿Qué porcentaje de las ventas de clientes "Empresarial" se pagó por transferencia vs. clientes "Individual"? (normaliza los valores de metodo_pago antes de comparar).
select clientes.cliente_tipo,count(metodo_pago.metodo_pago) from ventas
inner join clientes on ventas.id_cliente = clientes.id_cliente
inner join metodo_pago on ventas.id_metodo_pago = metodo_pago.id_metodo_pago
group by cliente_tipo
;

select clientes.cliente_tipo,count(metodo_pago.metodo_pago)from ventas
inner join clientes on ventas.id_cliente = clientes.id_cliente
inner join metodo_pago on ventas.id_metodo_pago = metodo_pago.id_metodo_pago
where metodo_pago.metodo_pago = 'transferencia'
group by cliente_tipo;

CREATE VIEW vista_pagos_por_tipo_cliente AS
SELECT
    c.cliente_tipo,
    COUNT(mp.metodo_pago) AS total_pagos
FROM ventas v
INNER JOIN clientes c
    ON v.id_cliente = c.id_cliente
INNER JOIN metodo_pago mp
    ON v.id_metodo_pago = mp.id_metodo_pago
GROUP BY c.cliente_tipo;
CREATE VIEW vista_transferencias_por_tipo_cliente AS
SELECT
    c.cliente_tipo,
    COUNT(mp.metodo_pago) AS total_transferencias
FROM ventas v
INNER JOIN clientes c
    ON v.id_cliente = c.id_cliente
INNER JOIN metodo_pago mp
    ON v.id_metodo_pago = mp.id_metodo_pago
WHERE mp.metodo_pago = 'transferencia'
GROUP BY c.cliente_tipo;

select * from vista_pagos_por_tipo_cliente;
select * from vista_transferencias_por_tipo_cliente;
select vista_transferencias_por_tipo_cliente.total_transferencias * vista_pagos_por_tipo_cliente.total_pagos
from vista_transferencias_por_tipo_cliente
inner join vista_pagos_por_tipo_cliente on vista_pagos_por_tipo_cliente.cliente_tipo