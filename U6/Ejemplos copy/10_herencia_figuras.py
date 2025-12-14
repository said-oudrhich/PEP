import math
from abc import ABC, abstractmethod

class Figura(ABC):
    """Clase base abstracta para figuras geométricas."""
    @abstractmethod
    def area(self):
        """Calcula el área de la figura."""
        pass

    @abstractmethod
    def perimetro(self):
        """Calcula el perímetro de la figura."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"

class Circulo(Figura):
    """Representa un círculo."""

    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, value):
        self._radio = value

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo(radio={self.radio})"

class Rectangulo(Figura):
    """Representa un rectángulo."""

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = value

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo(base={self.base}, altura={self.altura})"

class GestorFiguras:
    """Gestiona una colección de figuras."""

    def __init__(self):
        self.figuras = []

    def agregar_figura(self, figura):
        """Añade una figura a la colección."""
        if isinstance(figura, Figura):
            self.figuras.append(figura)
            print(f"Figura agregada: {figura}")
        else:
            print("Error: El objeto no es una figura válida.")

    def eliminar_figura(self, indice):
        """Elimina una figura por su índice."""
        if 0 <= indice < len(self.figuras):
            eliminada = self.figuras.pop(indice)
            print(f"Figura eliminada: {eliminada}")
        else:
            print("Error: Índice fuera de rango.")

    def mostrar_figuras(self):
        """Muestra todas las figuras en la colección."""
        print("\n--- Lista de Figuras ---")
        for i, figura in enumerate(self.figuras):
            print(f"{i}: {figura} | Área: {figura.area():.2f} | Perímetro: {figura.perimetro():.2f}")
        print("------------------------\n")

    def calcular_area_total(self):
        """Calcula la suma de las áreas de todas las figuras."""
        total = sum(f.area() for f in self.figuras)
        print(f"Área total de todas las figuras: {total:.2f}")
        return total

if __name__ == "__main__":
    # Código de prueba
    gestor = GestorFiguras()
    
    c1 = Circulo(5)
    r1 = Rectangulo(10, 4)
    c2 = Circulo(2.5)
    
    gestor.agregar_figura(c1)
    gestor.agregar_figura(r1)
    gestor.agregar_figura(c2)
    
    gestor.mostrar_figuras()
    
    gestor.calcular_area_total()
    
    gestor.eliminar_figura(1) # Eliminar el rectángulo
    
    gestor.mostrar_figuras()
    gestor.calcular_area_total()
