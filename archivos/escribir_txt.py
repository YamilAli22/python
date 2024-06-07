#escribir un archivo con el parametro "w" (write), si no existe, lo crea, si existe, lo sobreescribe
with open("/home/yamil/Escritorio/python/archivos/texto_de_yamil.txt", "w") as archivo:
    #archivo.write("Mira como te escribo papu")
    archivo.writelines(["Hola papa todo bien?\n", "Verdura\n"])
    #si hacemos otro, no se sobreescribe
    archivo.writelines(["bien y vos?\n", "palta\n"])

