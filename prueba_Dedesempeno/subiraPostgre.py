from sqlalchemy import create_engine


def cargar_postgresql(df, nombre_tabla):
    
    # Configuración de PostgreSQL
    usuario = "postgres"
    password = "1974"
    host = "localhost"
    puerto = "5434"
    base_datos = "BD_Ventas"

    # Crear cadena de conexión
    conn_string = f'postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}'

    # Crear engine
    engine = create_engine(conn_string)

    # Cargar DataFrame en PostgreSQL
    df.to_sql(
        name=nombre_tabla,
        con=engine,
        if_exists='append',
        index=False,
        chunksize=1000
    )

    print(
        f"Se cargaron {len(df)} registros "
        f"en la tabla '{nombre_tabla}'."
    )
    
    # cerrar la conexion
    engine.dispose()