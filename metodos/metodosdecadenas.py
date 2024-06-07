def metodos():

 cadena1 = "Hola Mundo"
 cadena2 = "Soy Yamil"

#upper convierte a mayusculas
 mayusc = cadena1.upper()
 print(mayusc)

#hay mas meotodos, lower convierte a minusculas
 minusc = cadena2.lower()
 print(minusc)

#capitalize, convierte la primera letra a mayuscula, y lo demas lo hace minuscula, ejemplo:
 cadena3 = "hola como andas?"
 primeraMayusc = cadena3.capitalize()
 print(primeraMayusc)

#find busca un valor que pidamos y nos devuelve el indice donde se encuentra, devuelve -1 si
#no encuentra nada
 busqueda = cadena2.find("Yamil")
 print(busqueda)

#index hace lo mismo pero si no encuentra nada tira error 

#isnumeric devuelve true si es numerico, false si no (ya sea tipo numero o un string de numeros)
 esNumerico = cadena1.isnumeric()
 print(esNumerico)

#alpha (numeric) devuelve true o false si es alfanumerico o no, si hay espacios da false.
 esAlfaNumerico = cadena2.isalpha()
 print(esAlfaNumerico)

#count busca una cadena en otra cadena, devuelve la cantidad de veces que coincida
 contarCoincidencias = cadena1.count("o")
 print(contarCoincidencias)

#len (es una función), devuelve la cantidad de caractares.
 contarCaracteres = len(cadena2)
 print(contarCaracteres)

#endswith y startwith, verifica si una cadena termina con o empieza con otra cadena o char dado
 terminaCon = cadena2.endswith("l")
 print(terminaCon)
 empiezaCon = cadena2.startswith("o")
 print(empiezaCon)

#replace, reemplaza una cadena por otra
 cadenaNueva = cadena2.replace("Yamil", "Yamil Ali")
 print(cadenaNueva)
 
#split separa cadenas con la cadena que le pasemos
 cadenaSeparada = cadena2.split()
 print(cadenaSeparada)
metodos()