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


#LIMPIEZA

df = df.drop_duplicates()
df.to_csv('newCSV.csv',index=False)




# otra vez ETL

print(df[["name"]].value_counts())

print(df[df["name"]=='Bounce'])

print(df[["developer"]].value_counts())