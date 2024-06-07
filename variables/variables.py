def variables():
    datos_tupla = ("Yamil", "Ali", 24)
    datos_lista = ["Yamil", "Ali", 24]

    #desempaquetando datos (tambien funciona para sets)
    nombre,apellido,edad = datos_tupla
    nombre1,apellido1,edad1 = datos_lista
    print(apellido)
    print(edad1)



variables()