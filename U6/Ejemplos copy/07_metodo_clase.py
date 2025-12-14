class Rectangulo:
    lados = 4  # Atributo de clase
    rectangulos = 0  # Atributo de clase para contar instancias

    def __init__(self, base, altura):
        self.base = base  # Atributo de instancia
        self.altura = altura  # Atributo de instancia
        Rectangulo.rectangulos += 1  # Incrementar el contador de instancias
      
    def area(self):
        return self.base * self.altura
   
    @classmethod
    def contar_rectangulos(cls):
        return cls.rectangulos
    
    
# Crear una instancia de Rectangulo
rectangulo1 = Rectangulo(5, 10)
rectangulo2 = Rectangulo(3, 6)
rectangulo3 = Rectangulo(4, 8)

print(Rectangulo.__name__)  # Salida: Rectangulo
print(type(rectangulo1).__name__)  # Salida: <class '__main__.Rectangulo'>
print(Rectangulo.__base__)  # Salida: <class 'object'>

    


    
   
