class Persona:
    def __init__(self, nombre, edad, nacionalidad="española"):
        self.nombre = nombre
        self.edad = edad
        self.nacionaliad = nacionalidad

alumna = Persona("Ana", 20, "argentina")
print(alumna.nombre)
print(alumna.nacionaliad)
alumna.edad = 22
print(alumna.edad)