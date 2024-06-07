#leer con csv
import csv
with open("/home/yamil/Escritorio/python/archivos/archivo.csv") as archivo:
    print(csv.reader(archivo))
    reader = csv.reader(archivo)
    for row in reader:
        print(row)