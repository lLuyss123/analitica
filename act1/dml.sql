CREATE TABLE clientes
(
    id_cliente    INT PRIMARY KEY,
    cliente_nombre  varchar,
    cliente_email varchar,
    cliente_tipo       varchar
);
CREATE TABLE metodo_pago
(
    id_metodo_pago    INT PRIMARY KEY,
    metodo_pago  varchar
);
CREATE TABLE producto
(
    id_producto    INT PRIMARY KEY,
    producto  varchar,
    categoria_producto varchar,
    precio_unitario float
);
CREATE TABLE sucursal
(
    id_sucursal    INT PRIMARY KEY,
    sucursal  varchar,
    ciudad_sucursal varchar
);

CREATE TABLE vendedor
(
    id_vendedor    INT PRIMARY KEY,
    vendedor  varchar
);
CREATE TABLE ventas
(
    id_venta    INT PRIMARY KEY,
    fecha_venta  date,
    cantidad INT,
    descuento_pct float,
    total_venta float,
    id_cliente int,
    id_sucursal int,
    id_vendedor int,
    id_producto int,
    id_metodo_pago int,



    CONSTRAINT fk_cliente
        FOREIGN KEY (id_cliente)
            REFERENCES clientes (id_cliente),
    CONSTRAINT fk_sucursal
        FOREIGN KEY (id_sucursal)
            REFERENCES sucursal (id_sucursal),
    CONSTRAINT fk_vendedor
        FOREIGN KEY (id_vendedor)
            REFERENCES vendedor (id_vendedor),
    CONSTRAINT fk_producto
        FOREIGN KEY (id_producto)
            REFERENCES producto (id_producto),
    CONSTRAINT fk_metodo_pago
        FOREIGN KEY (id_metodo_pago)
            REFERENCES metodo_pago (id_metodo_pago)
)
