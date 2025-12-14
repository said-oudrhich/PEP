class Persona:
    def __init__(self, nombre, edad, dni, nacionalidad="española"):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni  # Atributo privado
        self.nacionaliad = nacionalidad


    def saluda(self):
        print(f"Mi nombre es {self.nombre}, soy {self.nacionaliad}!")

    def muestra_edad(self):
        print(f"Mi edad es {self.edad - 5} años")

    def cambia_nacionalidad(self, nueva_nacionalida):
        self.nacionaliad = nueva_nacionalida

    def get_dni(self):
        return self.__dni
    
    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    def __eq__(self, otra):
        return self.edad == otra.edad

    def __lt__(self, otra):
        return self.edad < otra.edad
    
    def __gt__(self, otra):
        return self.edad > otra.edad
    
   
alumna1 = Persona("Ana", 20, "12345678A", "argentina")
alumna2 = Persona("Bea", 22, "87654321B", "chilena")    

print(alumna1._Persona__dni)  # Acceso al atributo privado mediante name mangling


print(alumna1==alumna2)  # Salida: False
print(alumna1 < alumna2)  # Salida: True
print(alumna1 > alumna2)  # Salida: False


