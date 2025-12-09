class AnimalTerrestre:
    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def peso(self):
        return self.__peso

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        else:
            self.__edad = nueva_edad

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso < 0:
            raise ValueError("El peso no puede ser negativo")
        else:
            self.__peso = nuevo_peso

    def saludar(self):
        print(
            f"Soy un animal llamado {self.nombre}, tengo {self.edad} anos y peso {self.peso} kilos."
        )


class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias

    @property
    def gestacion_dias(self):
        return self.__gestacion_dias

    @gestacion_dias.setter
    def gestacion_dias(self, nuevo_gestacion_dias):
        if nuevo_gestacion_dias < 0:
            raise ValueError("La gestación no puede ser negativa")
        else:
            self.__gestacion_dias = nuevo_gestacion_dias

    def saludar(self):
        print(
            f"Soy un mamifero llamado {self.nombre}, tengo {self.edad} anos y mi gestación es de {self.gestacion_dias} dias."
        )


class ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    @puede_volar.setter
    def puede_volar(self, nuevo_puede_volar):
        self.__puede_volar = nuevo_puede_volar

    def saludar(self):
        print(
            f"Soy un ave llamado {self.nombre}, tengo {self.edad} anos y puedo volar {self.puede_volar}."
        )


try:
    animal1 = AnimalTerrestre("juanito", 4, 10)
    animal1.saludar()

    animal2 = Mamifero("pepe", 2, 5, 30)
    animal2.saludar()

    animal3 = ave("pepe", 2, 5, True)
    animal3.saludar()
except Exception as e:
    print(e)
