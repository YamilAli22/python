#los condicionales de siempre xd
#ejemplo usando & e if anidado
def condicionales():
    dineroPorMes = 4500 
    canastaBasica = 5000
    gastoPorMes = 5000
    if dineroPorMes > canastaBasica | (dineroPorMes - gastoPorMes) > 0:
        print("Estas bien")
    elif dineroPorMes >= canastaBasica:
        if dineroPorMes - gastoPorMes == 0:
         print("Estas con lo justo")
    else:
        print("No llegas a fin de mes")
condicionales()