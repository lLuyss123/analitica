from sqlalchemy import create_engine, text
from normalizacion import *
# Configuración de PostgreSQL
usuario = "cayenas"
password = "123456a"
host = "localhost"
puerto = "5434"
base_datos = "postgres"

# Crear cadena de conexión

conn_string = f'postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}'

# Crear engine
engine = create_engine(conn_string)

print(games.columns.to_list())
with engine.begin() as conn:


    conn.execute(text("""
        DROP TABLE IF EXISTS games CASCADE;
        DROP TABLE IF EXISTS publishers CASCADE;
        DROP TABLE IF EXISTS developers CASCADE;
        DROP TABLE IF EXISTS names CASCADE;
    """))


    conn.execute(text("""


        CREATE TABLE names (
            id_name SERIAL,
            name VARCHAR(255) NOT NULL,

            CONSTRAINT pk_names
                PRIMARY KEY (id_name),

            CONSTRAINT uq_names_name
                UNIQUE (name)
        );

        CREATE TABLE developers (
            id_developer SERIAL,
            developer VARCHAR(255) NOT NULL,

            CONSTRAINT pk_developers
                PRIMARY KEY (id_developer),

            CONSTRAINT uq_developers_developer
                UNIQUE (developer)
        );

        CREATE TABLE publishers (
            id_publisher SERIAL,
            publisher VARCHAR(255) NOT NULL,

            CONSTRAINT pk_publishers
                PRIMARY KEY (id_publisher),

            CONSTRAINT uq_publishers_publisher
                UNIQUE (publisher)
        );

        CREATE TABLE games (
            id_game SERIAL,
            appid INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,
            developer VARCHAR(255),
            publisher VARCHAR(255),
            id_name INTEGER NOT NULL,
            id_developer INTEGER,
            id_publisher INTEGER,

            CONSTRAINT pk_games
                PRIMARY KEY (id_game),

            CONSTRAINT uq_games_appid
                UNIQUE (appid),

            CONSTRAINT fk_games_name
                FOREIGN KEY (id_name)
                REFERENCES names(id_name),

            CONSTRAINT fk_games_developer
                FOREIGN KEY (id_developer)
                REFERENCES developers(id_developer),

            CONSTRAINT fk_games_publisher
                FOREIGN KEY (id_publisher)
                REFERENCES publishers(id_publisher)
        );
    """))

# Subir los dataframes como tablas a PostgreSQL
name_games.to_sql(
    name='names',
    con=engine,
    if_exists='append',
    index=False
)

developer_games.to_sql(
    name='developers',
    con=engine,
    if_exists='append',
    index=False
)

publisher_games.to_sql(
    name='publishers',
    con=engine,
    if_exists='append',
    index=False
)

games.to_sql(
    name='games',
    con=engine,
    if_exists='append',
    index=False
)

stats_games.to_sql(
    name='stats',
    con=engine,
    if_exists='append',
    index=False
)

