#diccionario, literalmente un diccionario, key : value
def diccionario():
    dict0 = {
        'Nombre' : "Yamil",
        'Apellido' : "Ali",
        'Documento' : 41522678
    }
    print(dict0)
    print(dict0['Apellido'])
#creando un dict con la funcion dict
    dict1 = dict(nombre = "Yamil", apellido = "Ali", dni = 41522678)
    print(dict1)
    print(dict1['apellido'])

#creando un diccionario con fromkeys
    dict2 = dict.fromkeys(["nombre", "apellido", "dni"])
    print(dict2)
diccionario()