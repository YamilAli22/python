#FIBONACCI desde 0 hasta un numero dado
def fibonacci(num):
    a, b = 0, 1
    listafib = []
    for i in range(num):
        if b > num: return listafib
        else:
            listafib.append(b)
            a, b = b, a + b
    return listafib
resultado = fibonacci(5)
print(resultado)

    