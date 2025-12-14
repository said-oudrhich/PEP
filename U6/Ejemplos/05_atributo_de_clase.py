class Rectangulo:
    lados = 4  # Atributo de clase

    def __init__(self, base, altura):
        self.base = base  # Atributo de instancia
        self.altura = altura  # Atributo de instancia
      
    def area(self):
        return self.base * self.altura
    
    def mostrar_info(self):
        return f"Rectángulo de base {self.base} y altura {self.altura} y lados {self.lados}"
    
   

rectangulo1 = Rectangulo(5, 10)
print(f"Área del rectángulo: {rectangulo1.area()}") 
print(f"Número de lados del rectángulo: {Rectangulo.lados}")  #


rectangulo2 = Rectangulo(3, 4)
print(f"Área del segundo rectángulo: {rectangulo2.area()}")  
print(f"Número de lados del rectángulo: {Rectangulo.lados}")  #



