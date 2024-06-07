#leyendo un archivo
archivo = open("/home/yamil/Escritorio/python/archivos/texto_de_yamil.txt")
#print(archivo.read())

#leyendo una linea especifica
lineas = archivo.readlines()
print(lineas)

#cerrar el archivo
archivo.close()