"""
═══════════════════════════════════════════════════════════════════════════
GUÍA COMPLETA: PROGRAMACIÓN ORIENTADA A OBJETOS (POO) EN PYTHON
═══════════════════════════════════════════════════════════════════════════

Este archivo contiene TODOS los ejemplos y conceptos de POO que necesitas
para el examen. Usa Ctrl+F para buscar rápidamente lo que necesites.

ÍNDICE RÁPIDO (busca estos títulos):
1. CLASES BÁSICAS Y OBJETOS
2. CONSTRUCTOR __init__
3. ATRIBUTOS (de instancia y de clase)
4. MÉTODOS (de instancia, de clase, estáticos)
5. ENCAPSULACIÓN (atributos privados)
6. PROPERTIES (getters y setters)
7. HERENCIA
8. POLIMORFISMO
9. MÉTODOS ESPECIALES (__str__, __repr__, __lt__, __add__, etc.)
10. CLASES ABSTRACTAS (ABC)
11. COMPOSICIÓN Y ASOCIACIÓN
12. DECORADORES
13. ITERADORES
14. EJERCICIOS PRÁCTICOS COMPLETOS

═══════════════════════════════════════════════════════════════════════════
"""

from abc import ABC, abstractmethod
import random

# ═══════════════════════════════════════════════════════════════════════════
# 1. CLASES BÁSICAS Y OBJETOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("1. CLASES BÁSICAS Y OBJETOS")
print("=" * 80)

# EJEMPLO 1: Clase más simple
print("\n--- EJEMPLO 1: Clase vacía ---")

class MiClase:
    pass

objeto = MiClase()
print(f"Objeto creado: {objeto}")
print(f"Tipo: {type(objeto)}")

# EJEMPLO 2: Clase con atributos directos
print("\n--- EJEMPLO 2: Atributos directos ---")

class Persona:
    pass

p1 = Persona()
p1.nombre = "Ana"
p1.edad = 25

print(f"{p1.nombre} tiene {p1.edad} años")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 2. CONSTRUCTOR __init__
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("2. CONSTRUCTOR __init__")
print("=" * 80)

# EJEMPLO 1: Constructor básico
print("\n--- EJEMPLO 1: Constructor básico ---")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Carlos", 30)
p2 = Persona("María", 28)

print(f"{p1.nombre} tiene {p1.edad} años")
print(f"{p2.nombre} tiene {p2.edad} años")

# EJEMPLO 2: Constructor con valores por defecto
print("\n--- EJEMPLO 2: Valores por defecto ---")

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

prod1 = Producto("Laptop", 899.99)
prod2 = Producto("Mouse", 25.50, 50)

print(f"{prod1.nombre}: {prod1.precio}€ (stock: {prod1.stock})")
print(f"{prod2.nombre}: {prod2.precio}€ (stock: {prod2.stock})")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 3. ATRIBUTOS (de instancia y de clase)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("3. ATRIBUTOS DE INSTANCIA Y DE CLASE")
print("=" * 80)

# EJEMPLO 1: Atributos de instancia
print("\n--- EJEMPLO 1: Atributos de instancia ---")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo de instancia
        self.modelo = modelo    # Atributo de instancia

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

print(f"Coche 1: {coche1.marca} {coche1.modelo}")
print(f"Coche 2: {coche2.marca} {coche2.modelo}")

# EJEMPLO 2: Atributos de clase (compartidos por todas las instancias)
print("\n--- EJEMPLO 2: Atributos de clase ---")

class Animal:
    # Atributo de clase (compartido)
    numero_animales = 0
    
    def __init__(self, nombre, especie):
        self.nombre = nombre       # Atributo de instancia
        self.especie = especie     # Atributo de instancia
        Animal.numero_animales += 1  # Modificar atributo de clase

animal1 = Animal("Firulais", "Perro")
animal2 = Animal("Michi", "Gato")
animal3 = Animal("Piolin", "Pájaro")

print(f"Total de animales: {Animal.numero_animales}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 4. MÉTODOS (de instancia, de clase, estáticos)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("4. MÉTODOS")
print("=" * 80)

# EJEMPLO 1: Métodos de instancia
print("\n--- EJEMPLO 1: Métodos de instancia ---")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años")

p1 = Persona("Laura", 25)
p1.saludar()
p1.cumplir_anios()

# EJEMPLO 2: Métodos de clase (@classmethod)
print("\n--- EJEMPLO 2: Métodos de clase ---")

class Animal:
    numero_animales = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Animal.numero_animales += 1
    
    @classmethod
    def total_animales(cls):
        """Método de clase - accede a atributos de clase"""
        return cls.numero_animales
    
    @classmethod
    def crear_perro(cls, nombre):
        """Factory method - crea instancias predefinidas"""
        return cls(nombre)

a1 = Animal("Rex")
a2 = Animal("Luna")
print(f"Total de animales: {Animal.total_animales()}")

perro = Animal.crear_perro("Max")
print(f"Nuevo animal: {perro.nombre}")

# EJEMPLO 3: Métodos estáticos (@staticmethod)
print("\n--- EJEMPLO 3: Métodos estáticos ---")

class Matematicas:
    @staticmethod
    def suma(a, b):
        """No necesita self ni cls"""
        return a + b
    
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

print(f"5 + 3 = {Matematicas.suma(5, 3)}")
print(f"¿4 es par? {Matematicas.es_par(4)}")
print(f"¿7 es par? {Matematicas.es_par(7)}")

# Ejemplo completo con los 3 tipos
print("\n--- EJEMPLO 4: Los 3 tipos juntos ---")

class Empleado:
    empresa = "TechCorp"  # Atributo de clase
    total_empleados = 0
    
    def __init__(self, nombre, salario):
        self.nombre = nombre       # Atributo de instancia
        self.salario = salario
        Empleado.total_empleados += 1
    
    # Método de instancia
    def dar_aumento(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)
    
    # Método de clase
    @classmethod
    def contar_empleados(cls):
        return cls.total_empleados
    
    # Método estático
    @staticmethod
    def es_salario_valido(salario):
        return salario > 0

emp1 = Empleado("Ana", 30000)
emp2 = Empleado("Luis", 35000)

emp1.dar_aumento(10)
print(f"{emp1.nombre}: {emp1.salario}€")
print(f"Total empleados: {Empleado.contar_empleados()}")
print(f"¿50000 es válido? {Empleado.es_salario_valido(50000)}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 5. ENCAPSULACIÓN (atributos privados)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("5. ENCAPSULACIÓN - ATRIBUTOS PRIVADOS")
print("=" * 80)

print("\n--- Atributos privados con __ ---")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular         # Público
        self.__saldo = saldo_inicial   # Privado (__)
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"✓ Depositados {cantidad}€. Saldo: {self.__saldo}€")
        else:
            print("⚠ La cantidad debe ser positiva")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"✓ Retirados {cantidad}€. Saldo: {self.__saldo}€")
        else:
            print("⚠ Fondos insuficientes o cantidad inválida")
    
    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Carlos", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(f"Saldo actual: {cuenta.consultar_saldo()}€")

# No se puede acceder directamente a __saldo
# print(cuenta.__saldo)  # ❌ AttributeError

print()

# ═══════════════════════════════════════════════════════════════════════════
# 6. PROPERTIES (getters y setters)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("6. PROPERTIES - GETTERS Y SETTERS")
print("=" * 80)

print("\n--- Uso de @property ---")

class Rectangulo:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    # Getter con @property
    @property
    def ancho(self):
        return self.__ancho
    
    # Setter
    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self.__ancho = valor
        else:
            raise ValueError("El ancho debe ser positivo")
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self.__alto = valor
        else:
            raise ValueError("El alto debe ser positivo")
    
    @property
    def area(self):
        """Property de solo lectura (sin setter)"""
        return self.__ancho * self.__alto

rect = Rectangulo(5, 3)
print(f"Ancho: {rect.ancho}, Alto: {rect.alto}")
print(f"Área: {rect.area}")

# Modificar con el setter
rect.ancho = 10
print(f"Nueva área: {rect.area}")

# Ejemplo completo con validación
print("\n--- EJEMPLO: Animal con properties ---")

class Animal:
    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa")
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            raise ValueError("El peso debe ser positivo")

animal = Animal("Rex", 5, 20)
print(f"{animal.nombre}: {animal.edad} años, {animal.peso}kg")

animal.edad = 6
print(f"Ahora tiene {animal.edad} años")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 7. HERENCIA
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("7. HERENCIA")
print("=" * 80)

# EJEMPLO 1: Herencia básica
print("\n--- EJEMPLO 1: Herencia básica ---")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido")

class Perro(Animal):  # Hereda de Animal
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

perro = Perro("Rex")
gato = Gato("Michi")

perro.hacer_sonido()
gato.hacer_sonido()

# EJEMPLO 2: Herencia con super()
print("\n--- EJEMPLO 2: Herencia con super() ---")

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print(f"{self.marca} {self.modelo} arrancando...")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamar al constructor padre
        self.puertas = puertas
    
    def arrancar(self):
        super().arrancar()  # Llamar método padre
        print(f"Coche con {self.puertas} puertas listo")

coche = Coche("Toyota", "Corolla", 4)
coche.arrancar()

# EJEMPLO 3: Herencia completa
print("\n--- EJEMPLO 3: Sistema de animales terrestres ---")

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
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa")
    
    def saludar(self):
        print(f"Soy un animal llamado {self.nombre}, tengo {self.edad} años y peso {self.__peso} kilos")

class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias
    
    @property
    def gestacion_dias(self):
        return self.__gestacion_dias
    
    def saludar(self):
        print(f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años y mi gestación es de {self.__gestacion_dias} días")

class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar
    
    @property
    def puede_volar(self):
        return self.__puede_volar
    
    def saludar(self):
        volar_texto = "puedo volar" if self.__puede_volar else "no puedo volar"
        print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} años y {volar_texto}")

animal = AnimalTerrestre("Genérico", 3, 50)
mamifero = Mamifero("Elefante", 10, 5000, 645)
ave = Ave("Águila", 5, 6, True)

animal.saludar()
mamifero.saludar()
ave.saludar()

print()

# ═══════════════════════════════════════════════════════════════════════════
# 8. POLIMORFISMO
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("8. POLIMORFISMO")
print("=" * 80)

print("\n--- Mismo método, diferentes comportamientos ---")

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

# Polimorfismo: diferentes objetos, misma interfaz
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8)
]

for figura in figuras:
    print(f"{figura.__class__.__name__}: Área = {figura.area():.2f}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 9. MÉTODOS ESPECIALES (__str__, __repr__, __lt__, __add__, etc.)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("9. MÉTODOS ESPECIALES (MAGIC METHODS)")
print("=" * 80)

print("\n--- Métodos especiales ---")

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Representación en string
    def __str__(self):
        """Para print() - versión legible"""
        return f"Punto({self.x}, {self.y})"
    
    def __repr__(self):
        """Para repr() - versión técnica"""
        return f"Punto(x={self.x}, y={self.y})"
    
    # Comparaciones
    def __eq__(self, otro):
        """Igualdad =="""
        return self.x == otro.x and self.y == otro.y
    
    def __lt__(self, otro):
        """Menor que <"""
        return (self.x**2 + self.y**2) < (otro.x**2 + otro.y**2)
    
    # Operaciones aritméticas
    def __add__(self, otro):
        """Suma +"""
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        """Resta -"""
        return Punto(self.x - otro.x, self.y - otro.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"p1 - p2: {p1 - p2}")

# EJEMPLO 2: Animal con métodos especiales
print("\n--- EJEMPLO: Animal con operadores ---")

class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return f"Animal(nombre={self.nombre}, edad={self.edad}, peso={self.peso})"
    
    def __lt__(self, otro):
        """Comparar por edad"""
        return self.edad < otro.edad
    
    def __add__(self, otro):
        """Combinar dos animales (ejemplo ficticio)"""
        nuevo_nombre = f"{self.nombre}-{otro.nombre}"
        nueva_edad = self.edad + otro.edad
        nuevo_peso = self.peso + otro.peso
        return Animal(nuevo_nombre, nueva_edad, nuevo_peso)

a1 = Animal("Rex", 5, 20)
a2 = Animal("Luna", 3, 15)

print(a1)
print(a2)
print(f"a1 < a2: {a1 < a2}")

a3 = a1 + a2
print(f"Combinado: {a3}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 10. CLASES ABSTRACTAS (ABC)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("10. CLASES ABSTRACTAS")
print("=" * 80)

print("\n--- Clases abstractas con ABC ---")

class Personaje(ABC):
    """Clase base abstracta - no se puede instanciar"""
    
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        self._vida = max(0, valor)
    
    @abstractmethod
    def atacar(self, objetivo):
        """Método abstracto - debe implementarse en clases hijas"""
        pass

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza
    
    def atacar(self, objetivo):
        danio = self.fuerza + random.randint(0, 5)
        objetivo.vida -= danio
        print(f"{self.nombre} ataca y causa {danio} de daño")

class Mago(Personaje):
    def __init__(self, nombre, vida, poder_magico):
        super().__init__(nombre, vida)
        self.poder_magico = poder_magico
    
    def atacar(self, objetivo):
        danio = self.poder_magico + random.randint(0, 10)
        objetivo.vida -= danio
        print(f"{self.nombre} lanza un hechizo y causa {danio} de daño")

# No se puede instanciar Personaje directamente
# p = Personaje("Test", 100)  # ❌ TypeError

guerrero = Guerrero("Arthur", 100, 20)
mago = Mago("Merlin", 80, 25)

print(f"{guerrero.nombre}: {guerrero.vida} HP")
print(f"{mago.nombre}: {mago.vida} HP")

guerrero.atacar(mago)
print(f"{mago.nombre} queda con {mago.vida} HP")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 11. COMPOSICIÓN Y ASOCIACIÓN
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("11. COMPOSICIÓN Y ASOCIACIÓN")
print("=" * 80)

# EJEMPLO 1: Composición (una clase contiene a otra)
print("\n--- EJEMPLO 1: Composición ---")

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def arrancar(self):
        print(f"Motor de {self.potencia}HP arrancando...")

class Coche:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.motor = Motor(potencia)  # Composición: Coche TIENE-UN Motor
    
    def arrancar(self):
        print(f"{self.marca} arrancando...")
        self.motor.arrancar()

coche = Coche("Toyota", 150)
coche.arrancar()

# EJEMPLO 2: Composición con Arma
print("\n--- EJEMPLO 2: Guerrero con Arma ---")

class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio

class Guerrero:
    def __init__(self, nombre, arma):
        self.nombre = nombre
        self.arma = arma  # Composición
    
    def atacar(self):
        print(f"{self.nombre} ataca con {self.arma.nombre} (daño: {self.arma.danio})")

espada = Arma("Espada Larga", 50)
guerrero = Guerrero("Aragorn", espada)
guerrero.atacar()

# EJEMPLO 3: Asociación
print("\n--- EJEMPLO 3: Asociación (relación más débil) ---")

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor  # Asociación: Curso usa Profesor
    
    def info(self):
        print(f"Curso: {self.nombre} | Profesor: {self.profesor.nombre}")

prof = Profesor("Dr. García")
curso1 = Curso("Python Avanzado", prof)
curso2 = Curso("Bases de Datos", prof)

curso1.info()
curso2.info()

print()

# ═══════════════════════════════════════════════════════════════════════════
# 12. DECORADORES
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("12. DECORADORES")
print("=" * 80)

# EJEMPLO 1: Decorador básico
print("\n--- EJEMPLO 1: Decorador básico ---")

def mi_decorador(funcion):
    def envoltura():
        print("--- Antes de la función ---")
        funcion()
        print("--- Después de la función ---")
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()

# EJEMPLO 2: Decorador con argumentos
print("\n--- EJEMPLO 2: Decorador con argumentos ---")

def decorador_con_args(funcion):
    def envoltura(*args, **kwargs):
        print(f"Llamando a {funcion.__name__} con args={args}")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return envoltura

@decorador_con_args
def suma(a, b):
    return a + b

suma(5, 3)

# EJEMPLO 3: Decorador de tiempo
print("\n--- EJEMPLO 3: Medir tiempo de ejecución ---")

import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@cronometro
def operacion_lenta():
    time.sleep(0.1)
    return "Completado"

operacion_lenta()

print()

# ═══════════════════════════════════════════════════════════════════════════
# 13. ITERADORES
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("13. ITERADORES")
print("=" * 80)

# EJEMPLO 1: Clase iterable básica
print("\n--- EJEMPLO 1: Clase iterable ---")

class MiRango:
    def __init__(self, limite):
        self.limite = limite
    
    def __iter__(self):
        self._actual = 0
        return self
    
    def __next__(self):
        if self._actual < self.limite:
            valor = self._actual
            self._actual += 1
            return valor
        else:
            raise StopIteration

for num in MiRango(5):
    print(f"Número: {num}")

# EJEMPLO 2: Manada de animales iterable
print("\n--- EJEMPLO 2: Manada iterable ---")

class Manada:
    def __init__(self, animales=None):
        self.__animales = animales if animales else []
    
    def agregar(self, animal):
        self.__animales.append(animal)
    
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self.__animales):
            animal = self.__animales[self._index]
            self._index += 1
            return animal
        else:
            raise StopIteration

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Animal({self.nombre})"

manada = Manada([Animal("Rex"), Animal("Luna"), Animal("Max")])

print("Animales en la manada:")
for animal in manada:
    print(f"  - {animal}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 14. EJERCICIOS PRÁCTICOS COMPLETOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("14. EJERCICIOS PRÁCTICOS")
print("=" * 80)

# EJERCICIO 1: Sistema de biblioteca
print("\n--- EJERCICIO 1: Sistema de Biblioteca ---")

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"✓ '{self.titulo}' prestado")
        else:
            print(f"⚠ '{self.titulo}' ya está prestado")
    
    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"✓ '{self.titulo}' devuelto")
        else:
            print(f"⚠ '{self.titulo}' no estaba prestado")
    
    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.titulo}' de {self.autor} [{estado}]"

libro1 = Libro("1984", "George Orwell", "978-0451524935")
libro2 = Libro("El Quijote", "Cervantes", "978-8420412146")

print(libro1)
libro1.prestar()
print(libro1)
libro1.devolver()
print(libro1)

# EJERCICIO 2: Sistema de formas geométricas
print("\n--- EJERCICIO 2: Formas Geométricas ---")

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

formas = [Circulo(5), Rectangulo(4, 6)]

for forma in formas:
    nombre = forma.__class__.__name__
    print(f"{nombre}: Área={forma.area():.2f}, Perímetro={forma.perimetro():.2f}")

# EJERCICIO 3: Sistema de empleados con herencia
print("\n--- EJERCICIO 3: Sistema de Empleados ---")

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bonificacion):
        super().__init__(nombre, salario_base)
        self.bonificacion = bonificacion
    
    def calcular_salario(self):
        return self.salario_base + self.bonificacion

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, 0)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas

empleados = [
    EmpleadoTiempoCompleto("Ana", 3000, 500),
    EmpleadoPorHoras("Luis", 25, 120)
]

for emp in empleados:
    print(f"{emp.nombre}: {emp.calcular_salario()}€")

print("\n" + "=" * 80)
print("FIN DE LA GUÍA DE POO")
print("=" * 80)
print("Usa Ctrl+F para buscar: 'herencia', 'property', 'abstracta', 'decorador', etc.")
print("=" * 80)
