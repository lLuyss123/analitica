import pandas as pd
import numpy as np
from limpieza import *



"""
Carga un archivo CSV o Excel y devuelve un DataFrame.
"""

df = pd.read_csv('ventas.csv')

    
    
    
"""
Muestra información general del DataFrame.
"""

print("\n========== COLUMNAS ==========")
print(df.columns.tolist())

print("\n========== TIPOS DE DATOS ==========")
print(df.dtypes)

print("\n========== VALORES NULOS ==========")
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])


print("\n========== DUPLICADOS ==========")
print(df.duplicated().sum())
print(df[df.duplicated(keep=False)])

print("\n========== PRIMERAS FILAS ==========")
print(df.head())



limpiar_columnas(df)
print("\n========== COLUMNAS LIMPAS ==========")
print(df.columns.tolist())

df=eliminar_filas_vacias(df)
print("\n========== VALORES NULOS DESPUÉS DE ELIMINAR FILAS VACÍAS ==========")
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])

limpiar_espacios(df)


convertir_titulo(df, ['nombre','categoria','producto','ciudad','genero'])
print("\n========== PRIMERAS FILAS DESPUÉS DE LIMPIEZA ==========")
print(df.head())


print(df["ciudad"].value_counts())
print(df["categoría"].value_counts())
print(df["genero"].value_counts())
print(df["producto"].value_counts())
