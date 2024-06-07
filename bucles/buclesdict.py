def iterardict():
    diccionario = {
        "nombre" : "Yamil",
        "apellido" : "Ali",
        "edad" : 24,
        "dni" : 41522678
    }

#recorriendo el dict para obtener las claves y el valor con items()
    for datos in diccionario.items():
        key = datos[0]
        value = datos[1]
        print(f"""La clave es: {key} 
El valor es: {value}""")

iterardict()