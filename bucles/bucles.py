def bucle():
    animales = ["León", "Perro", "Gato", "Tiburón"]
    numeros = [3, 22, 7, 10]
#recorriendo la lista animales y mostrandoles por pantalla
    for animal in animales:
        print(animal)

#recorriendo las dos listas con for's anidados, esto va a generar todas las combinaciones posibles
    for animal in animales:
        for numero in numeros:
            print(animal, numero)

    print("---------")

#recorriendo dos listas con la funcion zip (deben tener la misma cantidad de elementos)
    for numero, animal in zip(animales, numeros):
        print(animal)
        print(numero)
    
#recorriendo una lista con la funcion range
    for num in range(10,15):
        print(num)

#usando enumerate, devuelve una tupla con el primer elemento que es el indice y el segundo el valor

    for num in enumerate(numeros):
        print(num[1])

#recorriendo una lista usando continue, para evitar mostrar un elemento
    lista_de_frutas = ["Banana", "Manzana", "Mandarina", "Naranja", "Frutilla"]
    for fruta in lista_de_frutas:
        if fruta == "Naranja":
            continue
        print(f"Me voy a comer una {fruta}")

    print("-----------")

#evitar que el bucle siga ejecutandose
    for fruta in lista_de_frutas:
        print(f"me voy a comer una {fruta}")
        if fruta == "Mandarina":
            break 

#recorrer una cadena de texto

    cadena_de_texto = "Hola mundo"
    for letra in cadena_de_texto:
        print(letra)

#for en una sola linea de codigo
    numeros = [1,2,3,4,5]
    numeros_duplicados = [x*2 for x in numeros]
    print(numeros_duplicados)

bucle()