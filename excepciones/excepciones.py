#manejo de excepciones
def sumar_dos():
    while True:
     a = input("numero 1: ")
     b = input("numero 2: ")
     try:
        resultado = int(a)+int(b)
     except Exception as e:
        print("Error, te pedi un numero")
        print(f"{e}")
     else:
      break
     #el finally se ejecuta siempre
     finally:
       print("Manejo de excepcion finalizado")
    return resultado
    
res = sumar_dos()
print(res)