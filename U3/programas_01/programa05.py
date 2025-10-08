"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""

# Variable global (accesible desde cualquier parte del código)
variable_global = "🌍 Soy una variable GLOBAL"


def funcion1():
    # Variable no local (definida en una función exterior)
    variable_no_local = "🌐 Soy una variable NO LOCAL"

    print("---- Dentro de funcion1 ----")
    print(variable_no_local)
    print(variable_global)
    print("-----------------------------\n")

    def funcion2():
        # Variable local (solo accesible dentro de esta función)
        variable_local = "🔹 Soy una variable LOCAL"

        print("---- Dentro de funcion2 ----")
        print(variable_local)
        print(variable_no_local)
        print(variable_global)
        print("-----------------------------\n")

    funcion2()


print("==== Inicio del programa ====\n")
funcion1()

print("==== Fuera de todas las funciones ====")
print(variable_global)
# Las siguientes líneas darían error porque las variables no están en este ámbito:
# print(variable_no_local)
# print(variable_local)
