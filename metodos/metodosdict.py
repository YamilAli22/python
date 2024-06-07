def metodos_dict():
#keys devuelve las clavesm, tambien sirve para iterar
    dict = {
        "nombre" : "Yamil",
        "apellido" : "Ali",
        "edad" : 24
    }
    keys = dict.keys()
    print(keys)

#get() devuelve el valor de una clave
    value = dict.get("nombre")
    print(value)

#clear elimina todos los elementos del dict
#dict.clear()

#pop elimina un elemento del dict
    dict.pop("edad")
    print(dict)

#items itera sobre el dict y te devuelve los elementos
    dict_iterable = dict.items()
    print(dict_iterable)


metodos_dict()