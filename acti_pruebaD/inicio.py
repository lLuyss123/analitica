#Cargue y exploracion de datos
import pandas as pd

df = pd.read_csv('steamspy_raw.csv')

print("\n========== COLUMNAS ==========")
print(df.columns.tolist())

print("\n========== TIPOS DE DATOS ==========")
print(df.dtypes)

print("\n========== VALORES NULOS ==========")
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])

print("\n========== DUPLICADOS ==========")
print(df.duplicated().sum())
print(df[df.duplicated()])

print("\n========== PRIMERAS FILAS ==========")
print(df.head())