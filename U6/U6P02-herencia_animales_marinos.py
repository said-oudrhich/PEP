from abc import ABC, abstractmethod

class AnimalMarino(ABC):
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))
          
    @abstractmethod
    def saluda(self):
        raise NotImplementedError
    
    @abstractmethod
    def sonido(self):
        raise NotImplementedError
    

class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)
        
    def saluda(self):
        print(f"Soy un delfin llamado {self.nombre}")

    def sonido(self):
        print("Clicks y silbidos")


class Tiburon(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)
        
    def saluda(self):
        print(f"Soy un tiburon llamado {self.nombre}")

    def sonido(self):
        print("No tiene un sonido audible característico")


try:

    animal1 = Delfin("Flipper")
    animal2 = Tiburon("Tiburon Blanco")
    animal3 = Delfin("Alex")
    animal4 = Tiburon("Mai")

    animales=[animal1, animal2, animal3, animal4]
    for animal in animales:
        animal.saluda()
        animal.sonido()

except Exception as e:
    print(e)
    


        
