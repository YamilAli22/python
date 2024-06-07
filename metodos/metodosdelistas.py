def metodos_de_listas():
    list = ["hola soy yamil", 24, 22, 6, 1999]
    cantidad_elementos = len(list)
    print(cantidad_elementos)

#append para agregar un elemento
    list.append("Yamil con Y")
    print(list)

#insert agrega un elemento en un indice especifico
    list.insert(2, "apellido: ali")
    print(list)

#agregar varios elementos, con extend
    list.extend(["Estudio Computación"])
    print(list)

#eliminar un elemento, con pop
    list.pop(4)
    print(list)

#remove, remueve un elemento de la lista por su valor
    list.remove("Yamil con Y")
    print(list)

#clear elimina todo
    #list.clear()

#sort ordena los elementos en forma ascendente, no funciona con cadenas de texto
#con el parametro reverse = True ordena al reves
    list1 = [1,3,4,0,8,5]
    list1.sort()
    print(list1)

#reverse invierte los elementos de la lista

    list.reverse()
    print(list)

metodos_de_listas()