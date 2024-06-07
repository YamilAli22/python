#creando mi propia excepcion
class miExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")


#lanzando mi propia excepcion
try:
#raise palabra clave para lanzar una excepcion    
    raise miExcepcion("Tara2")
except:
    print("Como sos tan tara2")
        