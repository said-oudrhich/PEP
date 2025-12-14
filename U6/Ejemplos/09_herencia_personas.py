class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre 

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def saluda(self):
        print(f"Mi nombre es {self._nombre}, y tengo {self._edad} años.")
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, ciclo):
        # super().__init__(nombre, edad)
        Persona.__init__(self, nombre, edad) 
        self.__ciclo = ciclo

    @property
    def ciclo(self):
        return self.__ciclo

    @ciclo.setter
    def ciclo(self, nuevo_ciclo):
        self.__ciclo = nuevo_ciclo  
    
    def saluda(self):
        #super().saluda()
        Persona.saluda(self)
        print(f"Estudio {self.__ciclo}.")

class Docente(Persona):
    def __init__(self, nombre, edad, modulo):
        super().__init__(nombre, edad)
        self.__modulo = modulo

    def saluda(self):
        super().saluda()
        print(f"Enseño {self.__modulo}.")
   
    
   
estudiante1 = Estudiante("Ana", 20, "DAW")
estudiante2 = Estudiante("Bea", 22, "DAM")
docente1 = Docente("Lucas", 35, "Programación")
docente2 = Docente("Diana", 40, "Bases de Datos") 

personas = [estudiante1, estudiante2, docente1, docente2]
for persona in personas:
    persona.saluda()
    print("---")

