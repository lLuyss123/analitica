


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("3_ventas.csv")
print("="*50)
print("Nombre de las columnas")
print(df.columns)
print("\n"+"="*50)
print(" Tipos de datos:")
print(df.dtypes)
print("\n"+"="*50)
print("Primeras 5 columnas de dataset")
print(df.head())
print("\n"+"="*50)
print("Tamaño del dataset:")
print(df.shape )
print("\n"+"="*50)
print(" Información general del dataset:")
print("",df.info())
print("\n"+"="*50)
print(" Estadisticas de las columnas númericas:")
print("",df.describe())


print("\n"+"="*50)
print(" Contar valores nulos que tienen cada columna:")
print(df.isnull().sum())



print("\n"+"="*50)
print("Datos cuya VENDEDOR son nulas")
print(df[df["vendedor"].isnull()])
print("\n"+"="*50)
print("Datos cuya REGION son nulas")
print(df[df["region"].isnull()])
print("\n"+"="*50)
print("Datos cuya cantidad son nulas")
print(df[df["cantidad"].isnull()])
print("\n"+"="*50)
print("Datos cuya PRECIO UNITARIO son nulas")
print(df[df["precio_unitario"].isnull()])
print("\n"+"="*50)
print("Datos cuya DESCUENTO son nulas")
print(df[df["descuento_pct"].isnull()])




print("\n"+"="*50)
print("Datos DUPLICADOS")
print(df.duplicated().sum())
print(df[df.duplicated()])
print(df[df.duplicated(keep=False)])



""" sin_duplicadoss """
df2= df.drop_duplicates()

print("\n"+"="*50)
print(df2["vendedor"].value_counts())

print("Despues de arreglar los nombres y salgan con mayusculas al inicio:")

df2["vendedor"]=df["vendedor"].str.title()
print(df2["vendedor"].value_counts())

print("Despues de arreglar a Maria gomez:")
df2["vendedor"]= df2["vendedor"].replace({
    "Maria Gómez": "María Gómez"
})

print(df2["vendedor"].value_counts())


""" cambiamos las cantidades negativas a + """

print("\n"+"="*50)
print("Datos cuya CANTIDAD son MENORES A 0")
print(df2[df2["cantidad"]<0])
df2.loc[df2["cantidad"] < 0, "cantidad"] *= -1

print("\n"+"="*50)
""" cambiamos los precios unitarios nulos ya que esto afecta el analizis """
print(df2.groupby("producto")["precio_unitario"].mean())
promedios= df2.groupby("producto")["precio_unitario"].transform("mean")

df2["precio_unitario"]=df2["precio_unitario"].fillna(promedios)



df2=df2.dropna(subset=["vendedor","region"])

df2.fillna({"descuento_pct": 0}, inplace=True)

print(df2)

