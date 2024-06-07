import re

texto = '''Hola tito, como estas? linea numero 1. 
Esta es la 2da. linea de texto
Esta es la 3era. y ultima'''

#haciendo una busqueda simple
#resultado = re.findall("Esta", texto)

#print(resultado)

#\d busca digitos numeros del 0 al 9

resultado = re.findall(r"\d", texto)
print(resultado)

#\D busca TODO menos digitos numericos

resultado2= re.findall(r"\D", texto)
print(resultado2)

#vemos que al usar la expresion contrario, osea en mayusculas, realiza la operacion contraria, je

#\w busca caracteres alfanumericos

resultado3 = re.findall(r"\w", texto)
print(resultado3)

#\W busca TODO menos caracteres alfanumericos

resultado4 = re.findall(r"\W", texto)
print(resultado4)

#\s busca espacios en blanco
resultado5 = re.findall(r"\s", texto)
print(resultado5)

#\S busca TODO menos espacios en blanco

#\. busca TODO menos saltos de linea

#\n busca saltos de linea

#\ cancela caracteres especiales
resultado6 = re.findall(r"\?", texto)
print(resultado6)

#armando una cadena que busque un nro seguido de un punto y un espacio
resultado7 = re.findall(f"\d\.\s", texto)
print(resultado7)

#buscando el comienzo de una linea con ^ 
resultado8 = re.findall(r"^Hola", texto)
print(resultado8)

#$ busca el final de una linea
resultado9 = re.findall(r"texto$", texto, flags=re.M)
print(resultado9)

#{n} busca n cantidad de veces el valor de la izquierda
resultado10 = re.findall(r"\d{3}", texto)
print(resultado10)

#{n,m} al menos n, como maximo m

#| busca una cosa o la otra