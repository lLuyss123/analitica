import pandas as pd
import numpy as np





    


# ============================================================
# 3. LIMPIAR NOMBRES DE COLUMNAS
# ============================================================

def limpiar_columnas(df):
    """
    Arreglar los nombres de las columnas.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


# ============================================================
# 4. ELIMINAR FILAS COMPLETAMENTE VACÍAS
# ============================================================

def eliminar_filas_vacias(df):
    """
    Elimina filas donde todas las columnas están vacías.
    """
    df= df.dropna(how="all")
    return df





# ============================================================
# 6. LIMPIAR ESPACIOS EN COLUMNAS DE TEXTO
# ============================================================

def limpiar_espacios(df):
    """
    Elimina espacios al principio y al final
    de las columnas de texto.   
       
    """

    columnas_texto = df.select_dtypes(
        include="object"
    ).columns

    for columna in columnas_texto:
        df[columna] = df[columna].str.strip()

    return df


# ============================================================
# 7. CONVERTIR TEXTO A TITULO
# ============================================================

def convertir_titulo(df, columnas):
    """
    Convierte las columnas indicadas a título.
    """

    for columna in columnas:
        df[columna] = df[columna].str.title()

    return df


# ============================================================
# 8. CONVERTIR TEXTO A MAYÚSCULAS
# ============================================================

def convertir_mayusculas(df, columnas):
    """
    Convierte las columnas indicadas a mayúsculas.
    """

    for columna in columnas:
        df[columna] = df[columna].str.upper()

    return df


# ============================================================
# 9. ELIMINAR DUPLICADOS
# ============================================================

def eliminar_duplicados(df):
    """
    Elimina filas duplicadas.

    Si columnas=None:
        busca duplicados en toda la fila.

    Si se indican columnas:
        busca duplicados únicamente utilizando esas columnas.
    """

    df = df.drop_duplicates(
        keep='first'
    )

    return df


# ============================================================
# 10. CONVERTIR COLUMNAS A NUMÉRICAS
# ============================================================

def convertir_numerica(df, columna):
    """
    Convierte las columnas indicadas a números.

    Los valores que no puedan convertirse
    serán transformados en NaN.
    """
    df[columna]=pd.to_numeric(
            df[columna],
            errors="coerce"
        )

    return df


# ============================================================
# 11. CONVERTIR COLUMNAS A FECHA
# ============================================================

def convertir_fecha(df, columna):
    """
    Convierte las columnas indicadas a datetime.
    """
    df[columna] = pd.to_datetime(
        df[columna],
        errors="coerce"
    )

    return df


# ============================================================
# 12. ELIMINAR FILAS CON NULOS
# ============================================================

def eliminar_nulos(df, columnas=None):
    """
    Elimina filas con valores nulos.

    Si columnas=None:
        elimina filas que tengan NaN en cualquier columna.

    Si se especifican columnas:
        solamente considera esas columnas.
    """

    return df.dropna(subset=columnas)


# ============================================================
# 13. RELLENAR NULOS
# ============================================================

def rellenar_nulos(df, columna, valor):
    """
    Rellena los valores NaN de una columna
    con el valor indicado.
    """

    df[columna] = df[columna].fillna(valor)

    return df


# ============================================================
# 14. RELLENAR NULOS CON MEDIA
# ============================================================

def rellenar_con_media(df, columna):
    """
    Rellena valores nulos usando la media.
    """

    media = df[columna].mean()

    df[columna] = df[columna].fillna(media)

    return df


# ============================================================
# 15. RELLENAR NULOS CON MEDIANA
# ============================================================

def rellenar_con_mediana(df, columna):
    """
    Rellena valores nulos usando la mediana.
    """

    mediana = df[columna].median()

    df[columna] = df[columna].fillna(mediana)

    return df

# ============================================================
# 16. REGLA DE 3
# ============================================================

def completar_venta(df, cantidad, precio, total):

    for indice, fila in df.iterrows():

        # Cuando falta el total
        if pd.isna(fila[total]):
            df.loc[indice, total] = (
                fila[cantidad] * fila[precio]
            )

        # Cuando falta la cantidad
        elif pd.isna(fila[cantidad]):
            df.loc[indice, cantidad] = (
                fila[total] / fila[precio]
            )

        # Cuando falta el precio
        elif pd.isna(fila[precio]):
            df.loc[indice, precio] = (
                fila[total] / fila[cantidad]
            )

    return df


# ============================================================
# 17. NORMALIZAR CATEGORÍAS
# ============================================================

def normalizar_categorias(df, columna, equivalencias):
    """
    Reemplaza diferentes valores por una categoría estándar.

    Ejemplo:

    {
        "M": "Masculino",
        "Hombre": "Masculino"
    }
    """

    df[columna] = df[columna].replace(
        equivalencias
    )

    return df


# ============================================================
# 18. ESTADÍSTICAS NUMÉRICAS
# ============================================================

def estadisticas_numericas(df):
    """
    Muestra estadísticas de las columnas numéricas.
    """

    print("\n========== ESTADÍSTICAS ==========")

    print(
        df.describe()
    )

# ============================================================
# 21. VALIDAR DATASET
# ============================================================

def validar_dataset(df):
    """
    Realiza una revisión final del dataset.
    """

    print("\n====================================")
    print("       VALIDACIÓN FINAL")
    print("====================================")

    print(f"\nFilas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    print("\nNulos:")
    print(df.isnull().sum())

    print("\nDuplicados:")
    print(df.duplicated().sum())

    print("\nTipos de datos:")
    print(df.dtypes)


# ============================================================
# 22. GUARDAR DATASET
# ============================================================

def guardar_dataset(df, ruta):
    """
    Guarda el DataFrame como CSV.
    """

    df.to_csv(
        ruta,
        index=False
    )

    print(f"\nDataset guardado en: {ruta}")