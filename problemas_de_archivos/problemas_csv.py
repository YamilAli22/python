#cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("/home/yamil/Escritorio/python/problemas_de_archivos/archivo.csv")
#cambiarlo a str
df["edad"] = df["edad"].astype(str)
print(df["edad"])

#reemplazar un valor
df["nombre"].replace("yamil", "kpo", inplace=True)
print(df["nombre"])

#eliminar datos con filas faltantes
df = df.dropna()
print(df)

#df.dropduplicates elimina filas duplicadas