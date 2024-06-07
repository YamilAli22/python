def es_primo(numero):
    if numero == 2:
        return True
    if numero < 2 or numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2): #La idea es que si un número no es primo, debe tener un divisor en el rango de 2 a su raíz cuadrada
        if numero % i == 0:
            return False
    return True

def primos_hasta(num):
    lista = []
    if num == 2: lista.append(2)

    for i in range(2, num):
        if es_primo(i):
            lista.append(i)
    return lista

lista_de_primos = primos_hasta(13)
print(lista_de_primos)