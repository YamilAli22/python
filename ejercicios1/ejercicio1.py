#el curso mas rapido dura 2.5hs, el mas lento 7hs, el promedio 4hs, el curso q estoy viendo 1.5hs
#a)cuanta dif en porcentaje hay entre el mas lento y el que estoy viendo? y entre el mas rapido? y el promedio?

def diferencia_entre_cursos():
    curso_mas_lento = float(7)
    curso_mas_rapido = float(2.5)
    curso_promedio = float(4)
    curso_actual = float(1.5)
    dif_actual_lento = round(100 - (curso_actual/curso_mas_lento * 100), 2)
    dif_actual_rapido = 100 - (curso_actual/curso_mas_rapido * 100)
    dif_actual_promedio = 100 - (curso_actual/curso_promedio * 100)
    print(f"""Diferencia entre el actual y el mas lento: {dif_actual_lento}%
Diferencia entre el actual y el mas rapido: {dif_actual_rapido}%
Diferencia entre el actual y el promedio: {dif_actual_promedio}%""")
diferencia_entre_cursos()

#b) porcentaje de material inservible que se reduce en el promedio de los cursos y el curso actual
print("---------------")


def material_inservible():
    crudo_curso_promedio = float(5)
    crudo_curso_actual = float(3.5)
    curso_promedio = float(4)
    curso_actual = float(1.5)
    porcentaje_mat_inservible = 100 - ((curso_promedio*100)/crudo_curso_promedio)
    porcentaje_mat_inservible2 = round(100 - ((curso_actual*100)/crudo_curso_actual), 2)
    print(f"""El porcentaje reducido en el curso promedio es de: {porcentaje_mat_inservible}%
El porcentaje reducido en el curso actual es de: {porcentaje_mat_inservible2}%""")
material_inservible()

print("---------------")

#c) ver 10hs del curso actual a cuantas horas de otros cursos equivale?

def equivalencia_entre_cursos():
    curso_mas_lento = float(7)
    curso_mas_rapido = float(2.5)
    curso_promedio = float(4)
    curso_actual = float(1.5)
    print(f"""Ver 10 hs del curso actual equivale a ver: {round(curso_promedio/curso_actual*10, 2)} del curso promedio
y: {round(curso_mas_lento/curso_actual*10, 2)} del curso mas lento
y: {round(curso_mas_rapido/curso_actual*10, 2)} del curso mas rapido""")
equivalencia_entre_cursos()
#round sirve para redondear, en este caso a 2 decimales