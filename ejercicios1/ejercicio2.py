#si una persona promedio habla 2 palabras por segundo
#a)Pedirle al usuario que diga una frase, calcular cuanto tardaria en decir esa frase y la cantidad de palabras

def palabras_por_segundo():
    frase = input("Ingrese una frase: ")
    #split divide la cadena en palabras (crea una lista con cada palabra)
    palabras_de_la_frase = frase.split()
    #ahora uso len y me devuelve la cantidad de elemento de la lista, osea la cantidad de palabras
    cantidad_de_palabras = len(palabras_de_la_frase)
    palabras_por_s = cantidad_de_palabras/2
    print(palabras_por_s)

    print(f"La cantidad de palabras es: {cantidad_de_palabras}")

    if cantidad_de_palabras > 120:
        print("Para flaco tampoco te pedi un testamento")
    else:
        print("Bien, corta la bocha")
palabras_por_segundo()