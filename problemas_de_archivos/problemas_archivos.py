#dos listas, una con nombres, otras con apellidos

nombres = ["Yamil", "Franca", "Chaira", "Ana"]
apellidos = ["Ali", "Sartoris", "Calfa", "Bossio"]

#guardar esta info en un txt optimamente

with open("/home/yamil/Escritorio/python/problemas_de_archivos/texto.txt", "w") as archivo:
    archivo.writelines("Los datos son:\n\n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n") for n,a in zip(nombres,apellidos)]