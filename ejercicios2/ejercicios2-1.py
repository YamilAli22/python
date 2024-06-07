#a) un alumno profesor, uno asistente, pedir los nombres de quienes fueron a clases y ordenarlos
#de mayor a menor

def clases(cantidad_de_compañeros):
    alumnos = list() #inicializo la lista vacia
    i = 1
    while i <= cantidad_de_compañeros:
        nombres = input("Ingrese su nombre: ")
        edades = int(input("Ingrese su edad: ")) #convierto el input a entero
        alumno = (nombres, edades)
        alumnos.append(alumno)
        i+=1
    
    alumnos.sort(key = lambda x: x[1]) #ordeno las edades de menor a mayor, usando la funcion anonomima lambda
    print(alumnos) #muestro la lista de edades por pantalla

    asistente = alumnos[0][0] #[(1,2), (1,2) ...]
    profesor = alumnos[-1][0]
    return asistente, profesor

asistente, profesor = clases(int(input("Ingrese la cantidad de alumnos: ")))
        
print(f"el asistente es: {asistente}, el profesor es: {profesor}")