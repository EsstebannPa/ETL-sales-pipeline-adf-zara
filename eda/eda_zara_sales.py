#Análisis exploratorio inicial de Pipeline ETL Zara: 

#Importación de librerías y primera visualización del CSV
import pandas as pd
import matplotlib.pyplot as plt

raw_df = pd.read_csv("../data/raw/zara_sales_june.csv")
print("Primera vista del CSV:")
print(raw_df.info())

#Creación y reestructuración de DataFrame con nuevo delimitador identificado ";"
df = pd.read_csv("../data/raw/zara_sales_june.csv", sep=";")
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

#Visualiación rápida del DataFrame
print("\nTamaño del DataFrame:\n", df.shape)
print("\n Nombre de las columnas:\n", tuple(df.columns))
print("Vista preliminar de datos, primeras líneas:\n", df.head())
print("\nInformación del esquema:\n", df.info())
print("\nResumen estadístico:\n", df.describe())

#Validación del DataFrame
print("\nConteo de valores nulos por columna:\n", df.isnull().sum())
null_rows = df[df.isnull().any(axis=1)]
print("\nTotal de filas con valores nulos:", len(null_rows))
print(df.loc[60], df.loc[72])

#Análisis básico del DataFrame.

if 'name' in df.columns and 'sales_volume' in df.columns:
    print("Los 5 mejores productos vendidos: ")
    df_top_sales = df.groupby(['name'])['sales_volume'].sum().sort_values(ascending=False)
    print(df_top_sales.head(5))

#Visualización breve
df_top_sales.head(5).plot(kind="bar", figsize=(10,6), color="yellow", edgecolor="black")
plt.title("Mejores 5 productos vendidos - ZARA")
plt.ylabel("Total de Ventas")
plt.xlabel("Producto")
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()
