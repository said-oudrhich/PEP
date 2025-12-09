class Animal:

    __numero_animales = 0

    def __init__(self, nombre, especie, edad, id_chip, peso=60):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip
        self.__peso = peso
        Animal.__numero_animales += 1

    @property
    def id_chip(self):
        return self.__id_chip

    @id_chip.setter
    def id_chip(self, nuevo_id_chip):
        if isinstance(nuevo_id_chip, str):
            print("Se ha cambiado el id_chip")
            self.__id_chip = nuevo_id_chip
        else:
            raise Exception("El id_chip debe ser una cadena de caracteres")

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso > 0:
            print("Se ha cambiado el peso")
            self.__peso = nuevo_peso
        else:
            raise Exception("El peso debe ser mayor que 0")

    @classmethod
    def numero_animales(cls):
        return cls.__numero_animales

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 2

    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad = self.edad + 1


try:
    animal1 = Animal("juanito", "Perro", 4, "ejemplo1", 10)
    animal2 = Animal("pepe", "Gato", 2, "ejemplo2", 5)

    print(Animal.numero_animales())
    print(animal1.id_chip)
    animal1.id_chip = "regwfwdfwf"
    print(animal1.id_chip)

    print(animal2.peso)
    animal2.peso = 10
    print(animal2.peso)

    if Animal.es_mayor_de_edad(3):
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

except Exception as e:
    print(e)
