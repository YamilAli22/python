import pandas as pd

#usando la funcion read_csv para leer el archivo
df = pd.read_csv("/home/yamil/Escritorio/python/archivos/archivo.csv")

#obteniendo los datos de la columna nombre
#print(df["nombre"])

#ordenando el archivo por edades
df_ordenado = df.sort_values("edad")
print(df_ordenado)

#accediendo a las filas con head
primeras_filas = df.head(2)
print(primeras_filas)

#con tail podemos acceder a las ultimas

#obteniendo la cantidad de filas y de columnas con shape
#filas_totales,columnas_totales = df.shape()

#obteniendo datos estadisticos del dataframe
df_info = df.describe()
print(df_info)

#accediendo a un elemento especifico del df con loc
elemento_especifico = df.loc[2, "edad"]
print(elemento_especifico)

#accediendo con iloc (solo con indices)

elemento_especifico2 = df.iloc[2,2]
print(elemento_especifico2)