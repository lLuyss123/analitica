import pandas as pd
import numpy as np

dfOriginal = pd.read_csv('ventas_desnormalizado.csv')

# Copia del DataFrame para evitar advertencias de vista
df = dfOriginal.copy()

# contar incompletos
incompletos = dfOriginal.isna().any(axis=1).sum()

# rellenar los valores nulos con desconocido de la columna cliente_email
df.loc[:, "cliente_email"] = df["cliente_email"].fillna("desconocido")

# rellenar los valores de la columna "total_venta" con la mediana de la columna
df.loc[:, "total_venta"] = df["total_venta"].fillna(df["total_venta"].median())

# normalizar los datos
df["sucursal"] = df["sucursal"].str.strip().str.lower()
df["metodo_pago"] = df["metodo_pago"].str.strip().str.lower()
df["cliente_nombre"] = df["cliente_nombre"].str.strip().str.capitalize()

# reemplazamos los espacios por _ 
df["sucursal"] = df["sucursal"].str.replace(" ", "_")
df["producto"] = df["producto"].str.replace(" ", "_")

# Convertimos la fecha a tipo datetime
df["fecha_venta"] = pd.to_datetime(df["fecha_venta"], format='mixed', dayfirst=True)





##  ENTIDADES NORMALIZADAS

# Entidad de Clientes 
clientes = df[["cliente_nombre", "cliente_email", "cliente_tipo"]].drop_duplicates(subset=["cliente_nombre"]).reset_index(drop=True)
clientes["id_cliente"] = clientes.index + 1
clientes = clientes[["id_cliente", "cliente_nombre", "cliente_email", "cliente_tipo"]]

# Entidad de sucursales
sucursal = df[["sucursal","ciudad_sucursal"]].drop_duplicates(subset=["sucursal"]).reset_index(drop=True)
sucursal["id_sucursal"] = sucursal.index + 1
sucursal = sucursal[["id_sucursal", "sucursal", "ciudad_sucursal"]]

# Entidad de vendedor
vendedor = df[["vendedor"]].drop_duplicates(subset=["vendedor"]).reset_index(drop=True)
vendedor["id_vendedor"] = vendedor.index + 1
vendedor = vendedor[["id_vendedor", "vendedor"]]

# Entidad de producto
producto = df[["producto", "categoria_producto", "precio_unitario"]].drop_duplicates(subset=["producto"]).reset_index(drop=True)
producto["id_producto"] = producto.index + 1
producto = producto[["id_producto", "producto", "categoria_producto", "precio_unitario"]]

# Entidad de metodo de pago
metodo_pago = df[["metodo_pago"]].drop_duplicates(subset=["metodo_pago"]).reset_index(drop=True)
metodo_pago["id_metodo_pago"] = metodo_pago.index + 1
metodo_pago = metodo_pago[["id_metodo_pago", "metodo_pago"]]

# Entidad de ventas
ventas = df[["fecha_venta", "cliente_nombre", "sucursal", "vendedor", "producto", "metodo_pago", "cantidad", "descuento_pct", "total_venta"]].copy()
ventas.loc[:, "id_venta"] = ventas.index + 1

ventas = ventas.merge(clientes[["id_cliente", "cliente_nombre"]], on="cliente_nombre", how="left")
ventas = ventas.merge(sucursal[["id_sucursal", "sucursal"]], on="sucursal", how="left")
ventas = ventas.merge(vendedor[["id_vendedor", "vendedor"]], on="vendedor", how="left")
ventas = ventas.merge(producto[["id_producto", "producto"]], on="producto", how="left")
ventas = ventas.merge(metodo_pago[["id_metodo_pago", "metodo_pago"]], on="metodo_pago", how="left")

ventas = ventas[["id_venta", "fecha_venta", "id_cliente", "id_sucursal", "id_vendedor", "id_producto", "id_metodo_pago", "cantidad", "descuento_pct", "total_venta"]]
ventas.columns = ["id_venta", "fecha_venta", "id_cliente", "id_sucursal", "id_vendedor", "id_producto", "id_metodo_pago", "cantidad", "descuento_pct", "total_venta"]





## PostgreSQL
from sqlalchemy import create_engine, text

# Configuración de la conexión
usuario = 'postgres'
password = '1974'
host = 'localhost'
puerto = '5434'
base_datos = 'BD_Ventas'

# Crear la cadena de conexión
conn_string = f'postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}'

# Crear el engine
engine = create_engine(conn_string)   

with engine.begin() as conn:
    conn.execute(text("""
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
        )"""))

# Subir los dataframes como tablas a PostgreSQL
clientes.to_sql(
    name='clientes',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)

sucursal.to_sql(
    name='sucursal',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)

vendedor.to_sql(
    name='vendedor',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)

producto.to_sql(
    name='producto',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)

metodo_pago.to_sql(
    name='metodo_pago',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)

ventas.to_sql(
    name='ventas',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1000
)   

# QUERY= """SELECT * FROM ventas;"  ""
# datosVentas = pd.read_sql(QUERY, engine)

# print(ventas.info())








# cerrar la conexion
engine.dispose()