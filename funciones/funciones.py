 
def first_function():
    print("Hello World")
first_function()


def second_function():
    print("Hola Mundo")
second_function()


def suma():
    x = 5
    y = 7
    z = x + y
    print(z)
suma()


#funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
     print(f"Hola {nombre}, como andas?")
    elif sexo == "hombre":
     print(f"Hola {nombre}, como andas man?")
saludar("Yamil", "hombre")
saludar("Franca", "mujer")

#funcion que retorna un valor
def suma_con_parametros(a,b,c):
    x = a + b + c
    return x

y = suma_con_parametros(2,3,4)
print(y)

#utilizando el parametro args
def parametros_indefinidos(*numeros):
   return sum(numeros)

resultado = parametros_indefinidos(1,4,5,7,3,2)
print(resultado)
