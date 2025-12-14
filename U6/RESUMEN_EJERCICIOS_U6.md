# 📚 Resumen de Ejercicios U6 - Programación Orientada a Objetos

## ✅ Estado de los Ejercicios

Todos los ejercicios están **completos y funcionando correctamente**. A continuación, se detalla cada uno con los conceptos de POO que aplican.

---

## 📝 U6P01 - Conceptos Básicos de Clases

### 📄 Archivo: [`U6P01-animales.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P01-animales.py)

### 🎯 Conceptos que se practican:

#### 1. **Atributos privados** (Encapsulación)

```python
self.__id_chip = id_chip    # Atributo privado con __
self.__peso = peso
```

- Los atributos con `__` son privados (name mangling)
- Solo accesibles mediante properties o métodos

#### 2. **Atributos de clase**

```python
__numero_animales = 0       # Atributo de clase (compartido)
```

- Se comparte entre todas las instancias
- Útil para contadores globales

#### 3. **Properties (getters y setters)**

```python
@property
def chip(self):
    return self.__id_chip

@chip.setter
def chip(self, nuevo_id_chip):
    if isinstance(nuevo_id_chip, str):
        self.__id_chip = nuevo_id_chip
    else:
        raise TypeError("El id_chip debe ser un string")
```

- Control de acceso a atributos privados
- Validación de datos en los setters

#### 4. **Métodos de clase** (@classmethod)

```python
@classmethod
def contar_animales(cls):
    return cls.__numero_animales
```

- Operan sobre la clase, no sobre instancias
- Primer parámetro es `cls` (la clase misma)

#### 5. **Métodos estáticos** (@staticmethod)

```python
@staticmethod
def es_mayor_de_edad(edad):
    return edad >= 2
```

- No necesitan acceso a `self` ni a `cls`
- Funciones utilitarias relacionadas con la clase

### 📊 Salida del programa:

```
0
1
2
a123
a123
Se ha cambiado el chip
a5222
99
Es mayor de edad
```

---

## 🎨 U6P02 - Decoradores Simples

### 📄 Archivo: [`U6P02-decorador.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P02-decorador.py)

### 🎯 Conceptos que se practican:

#### **Decoradores personalizados**

```python
def decorador(f):
    def funcion_nueva():
        print("Funcionalidad extra")
        f()
    return funcion_nueva

@decorador
def hola():
    print("Holaaaa")
```

- Los decoradores añaden funcionalidad sin modificar la función original
- Equivalente a: `hola = decorador(hola)`

### 📊 Salida del programa:

```
Funcionalidad inicial
Funcionalidad extra
Holaaaa
```

---

## 🐬 U6P02 - Herencia con Clases Abstractas (Animales Marinos)

### 📄 Archivo: [`U6P02-herencia_animales_marinos.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P02-herencia_animales_marinos.py)

### 🎯 Conceptos que se practican:

#### 1. **Clases Abstractas** (ABC)

```python
from abc import ABC, abstractmethod

class AnimalMarino(ABC):
    @abstractmethod
    def saluda(self):
        raise NotImplementedError
```

- No se pueden instanciar directamente
- Obligan a las subclases a implementar métodos abstractos

#### 2. **Herencia Simple**

```python
class Delfin(AnimalMarino):
    def __init__(self, nombre):
        super().__init__(nombre)  # Llama al constructor padre
```

#### 3. **Polimorfismo**

```python
animales = [animal1, animal2, animal3, animal4]
for animal in animales:
    animal.saluda()    # Cada uno ejecuta su versión
    animal.sonido()
```

- Diferentes clases responden al mismo método de forma distinta

### 📊 Salida del programa:

```
Soy un delfin llamado Flipper
Clicks y silbidos
Soy un tiburon llamado Tiburon Blanco
No tiene un sonido audible característico
Soy un delfin llamado Alex
Clicks y silbidos
Soy un tiburon llamado Mai
No tiene un sonido audible característico
```

---

## 🦁 U6P02 - Herencia y Sobrecarga de Operadores (Animales Terrestres)

### 📄 Archivo: [`U6P02-herencia_animales_terrestres.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P02-herencia_animales_terrestres.py)

### 🎯 Conceptos que se practican:

#### 1. **Herencia con jerarquía de clases**

```
AnimalTerrestre (clase base)
    ├── Mamifero (hereda de AnimalTerrestre)
    └── Ave (hereda de AnimalTerrestre)
```

#### 2. **Métodos Dunder (Magic methods)**

##### `__str__` - Representación legible

```python
def __str__(self):
    return f"AnimalTerrestre(nombre={self.nombre}, edad={self.edad}, peso={self.peso})"
```

##### `__lt__` - Operador de comparación (<)

```python
def __lt__(self, otro):
    return self.edad < otro.edad
```

##### `__add__` - Operador de suma (+)

```python
def __add__(self, otro):
    return AnimalTerrestre(
        self.nombre + "-" + otro.nombre,
        self.edad + otro.edad,
        self.peso + otro.peso
    )
```

#### 3. **Override de métodos** (Sobrescritura)

```python
# En la clase base
def saluda(self):
    print(f"Soy un animal terrestre llamado {self.nombre}")

# En Mamifero (sobrescribe)
def saluda(self):
    print(f"Soy un mamífero llamado {self.nombre}, gestación de {self.__gestacion_dias}")
```

### 📊 Salida del programa:

```
Soy un animal terrestre llamado Kuma y tengo 10 años
Soy un animal terrestre llamado Miu y tengo 5 años
Soy un mamimefero llamado Log, tengo 10 años y mi gestación es de 200
Soy un ave llamado Uff, tengo 4 años
 y puedo volar
AnimalTerrestre(nombre=Kuma, edad=10, peso=100)
AnimalTerrestre(nombre=Miu, edad=5, peso=6)
Mamifero(nombre=Log, edad=10, peso=90, gestacion_dias=200)
Ave(nombre=Uff, edad=4, peso=3, puede_volar=True)
False
True
AnimalTerrestre(nombre=Kuma-Miu, edad=15, peso=106)
```

---

## 🔄 U6P02 - Iteradores Personalizados (Manada)

### 📄 Archivo: [`U6P02-herencia_animales_iteradores.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P02-herencia_animales_iteradores.py)

### 🎯 Conceptos que se practican:

#### **Protocolo de Iteración**

```python
class Manada:
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__lista_animales):
            animal = self.__lista_animales[self._index]
            self._index += 1
            return animal
        else:
            raise StopIteration
```

- `__iter__`: Inicializa la iteración
- `__next__`: Devuelve el siguiente elemento
- `StopIteration`: Señal para detener el bucle

#### **Uso del iterador**

```python
manada = Manada([animal1, animal2, animal3, animal4])
for animal in manada:
    print(animal)
```

### 📊 Salida adicional (además de lo anterior):

```
AnimalTerrestre(nombre=Kuma, edad=10, peso=100)
AnimalTerrestre(nombre=Miu, edad=5, peso=6)
Mamifero(nombre=Log, edad=10, peso=90, gestacion_dias=200)
Ave(nombre=Uff, edad=4, peso=3, puede_volar=True)
```

---

## ⚔️ U6P03 - Juego de Combate (Composición y Asociación)

### 📄 Archivo: [`U6P03-juego.py`](file:///f:/DAW/2º/PEP/examen_martes/U6-Programación%20orientada%20a%20objetos.%20Frameworks%20Web/Prácticas/U6P03-juego.py)

### 🎯 Conceptos que se practican:

#### 1. **Composición** (relación "tiene-un")

```python
class Guerrero(Personaje):
    def __init__(self, nombre, vida, arma):
        super().__init__(nombre, vida)
        self._arma = arma  # El guerrero TIENE un arma
```

- El `Guerrero` contiene un objeto `Arma`
- Si el guerrero desaparece, su arma también

#### 2. **Asociación** (referencia externa)

```python
class Mago(Personaje):
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos  # Diccionario externo
```

- El `Mago` usa hechizos definidos externamente
- Los hechizos pueden existir independientemente

#### 3. **Clase Abstracta como base**

```python
class Personaje(ABC):
    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError
```

#### 4. **Polimorfismo en acción**

```python
def combate(a, b):
    # Funciona con cualquier tipo de Personaje
    a.atacar(b)
    b.atacar(a)
```

#### 5. **Properties con validación**

```python
@vida.setter
def vida(self, valor):
    # Evita vida negativa
    self._vida = max(0, valor)
```

### 📊 Salida del programa (varía por randomización):

```
--- COMIENZA EL COMBATE ---

--- Turno 1 ---
Arthur golpea con Espada larga y causa 24 de daño.
Merlin queda con 56 de vida.
Merlin lanza Rayo y causa 22 de daño.
Arthur queda con 78 de vida.

--- Turno 2 ---
Arthur golpea con Espada larga y causa 22 de daño.
Merlin queda con 34 de vida.
...

--- FIN DEL COMBATE ---

🏆 Arthur gana con 45 de vida restante.
```

---

## 📊 Tabla Comparativa de Conceptos

| Concepto                      | Ejercicios donde aparece | Importancia para el examen |
| ----------------------------- | ------------------------ | -------------------------- |
| **Atributos privados (`__`)** | U6P01, todos los demás   | ⭐⭐⭐ Muy importante      |
| **@property y @setter**       | U6P01, U6P02, U6P03      | ⭐⭐⭐ Muy importante      |
| **@classmethod**              | U6P01                    | ⭐⭐ Importante            |
| **@staticmethod**             | U6P01                    | ⭐⭐ Importante            |
| **Herencia simple**           | U6P02 (todos), U6P03     | ⭐⭐⭐ Muy importante      |
| **Clases abstractas (ABC)**   | U6P02-marinos, U6P03     | ⭐⭐⭐ Muy importante      |
| **Polimorfismo**              | U6P02-marinos, U6P03     | ⭐⭐⭐ Muy importante      |
| **Métodos dunder**            | U6P02-terrestres         | ⭐⭐⭐ Muy importante      |
| **Iteradores**                | U6P02-iteradores         | ⭐⭐ Importante            |
| **Decoradores**               | U6P02-decorador          | ⭐⭐ Importante            |
| **Composición**               | U6P03                    | ⭐⭐ Importante            |
| **Asociación**                | U6P03                    | ⭐ Complementario          |
| **super()**                   | Todos los de herencia    | ⭐⭐⭐ Muy importante      |

---

## 🎓 Conceptos Clave para el Examen

### 1️⃣ **Encapsulación**

- Atributos privados con `__`
- Acceso controlado con `@property`
- Validación en setters

### 2️⃣ **Herencia**

- `super().__init__()` para llamar al constructor padre
- Override de métodos
- Jerarquías de clases

### 3️⃣ **Polimorfismo**

- Misma interfaz, diferentes implementaciones
- Métodos abstractos (`@abstractmethod`)
- Duck typing

### 4️⃣ **Métodos Especiales (Dunder)**

- `__init__`: Constructor
- `__str__`: Representación en string
- `__lt__`, `__gt__`, `__eq__`: Comparaciones
- `__add__`, `__sub__`: Operadores aritméticos
- `__iter__`, `__next__`: Iteración

### 5️⃣ **Decoradores**

- `@property`, `@setter`, `@deleter`
- `@classmethod`: Métodos de clase
- `@staticmethod`: Métodos estáticos
- Decoradores personalizados

### 6️⃣ **Relaciones entre Objetos**

- **Composición**: "tiene-un" (fuerte)
- **Asociación**: "usa-un" (débil)
- **Herencia**: "es-un"

---

## 🚀 Ejercicios Ejecutados Correctamente

✅ **U6P01-animales.py** - Conceptos básicos
✅ **U6P02-decorador.py** - Decoradores
✅ **U6P02-herencia_animales_marinos.py** - ABC y polimorfismo
✅ **U6P02-herencia_animales_terrestres.py** - Sobrecarga de operadores
✅ **U6P02-herencia_animales_iteradores.py** - Iteradores personalizados
✅ **U6P03-juego.py** - Composición y sistema completo

---

## 💡 Recomendaciones de Estudio

1. **Entiende el flujo de herencia**: Rastrea cómo `super()` llama a los constructores padres
2. **Practica los métodos dunder**: Son muy comunes en exámenes
3. **Diferencia composición vs herencia**: Saber cuándo usar cada uno
4. **Memoriza los decoradores básicos**: `@property`, `@classmethod`, `@staticmethod`
5. **Practica crear clases abstractas**: Entiende por qué y cuándo usarlas

---

## 🎯 ¡Éxito en tu examen del martes!

Todos los ejercicios están funcionando. Repasa los conceptos y ejecuta los programas varias veces para entender el flujo.
