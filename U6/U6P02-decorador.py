def decorador(f):
    def funcion_nueva():
        print("Funcionalidad extra")
        f()
    return funcion_nueva


def funcion_inicial():
    print("Funcionalidad inicial")

@decorador
def hola():
    print ("Holaaaa")

funcion_inicial()
hola()