#diferentes funciones para listas

def lista():
    list = [1,2,3,4,5,6]
    print(list[:])
lista()

def lista2():
    list2 = [1,2,3,4,5,6]
    print(list2[3])
lista2()


#acceder a una porción de la lista
def lista3():
    list3 = ["Yamil", "Franca", "Ana", "Chaira"]
    print(list3[0:3])
    #también podemos hacer, y omitir el 0:
    print(list3[:3])
    #o:
    print(list3[1:3])
    #o
    print(list3[2:])
lista3()

#para agregar elementos a la lista
def append():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list.append("Juan")
    print(list[1:])
append()


#para agregar elementos en la posicion que querramos
def insert():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list.insert(2, "Tito")
    print(list[1:])
insert()


#para agregar varios elementos
def extend():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list.extend(["Tito", "Juan"])
    print(list[1:])
extend()
    

#para preguntar el indice de un elemento en una lista    
def index():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    print(list.index("Yamil"))
index()

#para saber si un elemento esta en la lista
def exists():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    print("Yamil" in list)
    print("Tito" in list)
exists()


#para eliminar un elemento
def remove():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list.remove("Yamil")
    print(list[:])
remove()
    
#para eliminar el ultimo elemento en una lista
def pop():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list.pop()
    print(list[:])
pop()

def suma_listas():
    list = ["Yamil", "Franca", "Ana", "Chaira"]
    list2 = ["Tito", "Picho"]
    list3 = list + list2
    print(list3[:])
suma_listas()