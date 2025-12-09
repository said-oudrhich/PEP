def decorador(funcion):
    def envoltura():
        print("Estoy antes")
        funcion()
        print("Estoy despues")

    return envoltura


@decorador
def mi_funcion():
    print("Estoy dentro")


mi_funcion()
