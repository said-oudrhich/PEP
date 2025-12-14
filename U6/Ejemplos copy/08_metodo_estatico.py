class Persona:
    def __init__(self, nombre, edad, nacionaliad="española"):
        self.nombre = nombre
        self.edad = edad
        self.nacionaliad = nacionaliad

    def saluda(self):
        print(f"Mi nombre es {self.nombre}, soy {self.nacionaliad}!")

    def muestra_edad(self):
        print(f"Mi edad es {self.edad - 5} años")

    def cambia_nacionalidad(self, nueva_nacionalida):
        self.nacionaliad = nueva_nacionalida

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

alumna = Persona("Ana", 20, "argentina")
print(Persona.__dict__)  # Muestra los atributos y métodos de la clase Persona


