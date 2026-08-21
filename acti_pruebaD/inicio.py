#Cargue y exploracion de datos
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


#LIMPIEZA Y TRANSFORMACION DE DATOS

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

# Convertir fechas
""" df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce") """


df.to_csv('newCSV.csv',index=False)




# otra vez ETL

print(df[["name"]].value_counts())

print(df[df["name"]=='Bounce'])

print(df[["developer"]].value_counts())