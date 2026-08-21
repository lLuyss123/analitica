#----------------------- Cargue y exploracion de datos
import pandas as pd

df = pd.read_csv('steamspy_raw.csv')

print("\n========== COLUMNAS ==========")
print(df.columns.tolist())

print("\n========== TIPOS DE DATOS ==========")
print(df.dtypes)

print("\n========== VALORES NULOS ==========")
print(df.isnull().sum())
nulos=df[df.isnull().any(axis=1)]
nulos.to_csv('nulos.csv',index=False)

print("\n========== DUPLICADOS ==========")
print(df.duplicated().sum())
duplicados=df[df.duplicated(subset="appid", keep=False)].sort_values("appid")
duplicados.to_csv('duplicados.csv',index=False)
print(df[df.duplicated()])

print("\n========== PRIMERAS FILAS ==========")
print(df.head())

print(df[df["name"].isna()])


#----------------- LIMPIEZA Y TRANSFORMACION DE DATOS

#Normalizamos los  nombres de las columnas
colums = df.columns.tolist()
df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

#Eliminamos los duplicados
df = df.drop_duplicates()

# Eliminar filas completamente vacías
df = df.dropna(how="all")

# Convertir tipos
df[["positive","negative","price","initialprice","discount","ccu"]] = df[["positive","negative","price","initialprice","discount","ccu"]].apply(
    pd.to_numeric,
    errors="coerce"
)

df["price"] = df["price"] / 100
df["initialprice"] = df["initialprice"] / 100

#Sacamos solo las columnas de tipo texto
columnas_texto = df.select_dtypes(
        include="object"
    ).columns

#Convertir los datos de las columnas a título de las columnas de texo
for columna in columnas_texto:
    df[columna] = df[columna].str.title()

#Quitar los espacios innecesarios de las columnas de las columnas de texto
for columna in columnas_texto:
    df[columna] = df[columna].str.strip()

# Convertir fechas
""" df["fecha"] = pd.to_datetime(df["fecha"], format='mixed', dayfirst=True) """

# Eliminamos las columnas que no nos sirven en nuestro analisis
df = df.drop(['average_forever', 'average_2weeks','median_forever','median_2weeks'], axis=1)


# Dividimos 
df[["owners_min", "owners_max"]] = df["owners"].str.split(' .. ', expand=True, n=1)

# Eliminamos las columnas que no nos sirven en nuestro analisis
df = df.drop(['owners'], axis=1)

# rellenar los valores nulos con desconocido en algunas columnas
df[["name","developer","publisher"]] = df[["name","developer","publisher"]].fillna("Desconocido")
df.to_csv('newCSV.csv',index=False)





# otra vez revisamos el dataset

print(df[["name"]].value_counts())


print(df[["developer"]].value_counts())

