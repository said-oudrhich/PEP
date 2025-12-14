# 📚 MASTER - UNIDADES 4, 5 y 6 - EXAMEN PYTHON

> **Documento de referencia completo para el examen de Python**  
> Incluye todos los conceptos, sintaxis y ejemplos de las unidades 4, 5 y 6

---

## 📑 ÍNDICE RÁPIDO

1. [UNIDAD 4: Cadenas de Caracteres](#unidad-4-cadenas-de-caracteres)
2. [UNIDAD 5: Ficheros CSV y JSON](#unidad-5-ficheros-csv-y-json)
3. [UNIDAD 6: Programación Orientada a Objetos](#unidad-6-programación-orientada-a-objetos)

---

# UNIDAD 4: CADENAS DE CARACTERES

## 🔹 1. CREACIÓN DE CADENAS

### Tipos de comillas

```python
# Comillas simples
cadena_simple = 'Esta es una cadena con comillas simples.'

# Comillas dobles
cadena_doble = "Esta es una cadena con comillas dobles."

# Comillas triples (para múltiples líneas)
cadena_triple = '''Esta es una cadena con comillas triples.
Puede abarcar múltiples líneas.'''
```

### Caracteres especiales

```python
# Saltos de línea y tabuladores
cadena = "Línea 1\nLínea 2\tCon tabulador"

# Cadenas crudas (raw strings) - ignoran caracteres especiales
cadena_cruda = r"Esta es una cadena cruda: \n \t \\"
```

## 🔹 2. ACCESO A CARACTERES

### Índices positivos y negativos

```python
cadena = "Python"

# Índices positivos (empiezan en 0)
primer_caracter = cadena[0]        # 'P'
ultimo_caracter = cadena[5]        # 'n'
ultimo_con_len = cadena[len(cadena)-1]  # 'n'

# Índices negativos (empiezan desde el final)
ultimo_negativo = cadena[-1]       # 'n'
primero_negativo = cadena[-6]      # 'P'
penultimo = cadena[-2]             # 'o'
```

## 🔹 3. FORMATO DE CADENAS

### Método .format()

```python
nombre = "Said"
curso = "2º DAW"
anno = 2025

# Usando .format()
mensaje = "Hola, me llamo {}, estoy en {} y el año es {}".format(nombre, curso, anno)

# Con índices
mensaje = "El {1} es después del {0}".format("lunes", "martes")

# Con nombres
mensaje = "Me llamo {n} y tengo {e} años".format(n="Ana", e=25)
```

### F-strings (recomendado)

```python
nombre = "Said"
curso = "2º DAW"
anno = 2025

# F-strings (Python 3.6+)
mensaje = f"Hola, me llamo {nombre}, estoy en {curso} y el año es {anno}"

# Con expresiones
edad = 20
mensaje = f"El año que viene tendré {edad + 1} años"
```

## 🔹 4. CONVERSIÓN DE TIPOS

### De otros tipos a string

```python
# Convertir números a cadenas
cadena_entero = str(44)           # "44"
cadena_decimal = str(2.5)         # "2.5"
cadena_booleano = str(True)       # "True"
```

## 🔹 5. OPERACIONES BÁSICAS

### Concatenación

```python
cadena1 = "Hola"
cadena2 = "Mundo"

# Con operador +
concatenada = cadena1 + " " + cadena2  # "Hola Mundo"
```

### Repetición

```python
cadena = "Hola"
repetida = cadena * 3  # "HolaHolaHola"
```

### Comparación lexicográfica

```python
cadena1 = "Hola"
cadena2 = "Mundo"

if cadena1 < cadena2:
    print(f'"{cadena1}" es menor que "{cadena2}"')  # Se comparan por orden alfabético
elif cadena1 > cadena2:
    print(f'"{cadena1}" es mayor que "{cadena2}"')
else:
    print("Son iguales")
```

### Operador in (pertenencia)

```python
cadena = "Hola Mundo"
subcadena = "Mundo"

if subcadena in cadena:
    print(f'"{subcadena}" está en "{cadena}"')  # True
```

## 🔹 6. SLICING (REBANADO)

### Sintaxis básica: [inicio:fin:paso]

```python
cadena = "Python"

# Extraer subcadena
subcadena = cadena[0:3]    # "Pyt" (de índice 0 a 2, el 3 no incluido)

# Caracteres en posiciones pares
pares = cadena[::2]        # "Pto" (cada 2 caracteres)

# Invertir cadena
invertida = cadena[::-1]   # "nohtyP"

# Desde inicio hasta posición
inicio = cadena[:3]        # "Pyt"

# Desde posición hasta final
final = cadena[3:]         # "hon"

# Con índices negativos
ultimos_3 = cadena[-3:]    # "hon"
```

## 🔹 7. ITERACIÓN

### Recorrer caracteres

```python
cadena = "Python"

# Recorrer cada carácter
for caracter in cadena:
    print(caracter)

# Con índice
for i in range(len(cadena)):
    print(f"Índice {i}: {cadena[i]}")

# Con enumerate
for indice, caracter in enumerate(cadena):
    print(f"Posición {indice}: {caracter}")
```

## 🔹 8. MÉTODOS DE CADENAS

### Métodos de transformación

```python
cadena = "  Hola Mundo  "

# Mayúsculas y minúsculas
cadena.upper()         # "  HOLA MUNDO  "
cadena.lower()         # "  hola mundo  "
cadena.capitalize()    # "  hola mundo  " (primera letra mayúscula)
cadena.title()         # "  Hola Mundo  " (primera letra de cada palabra)

# Eliminar espacios
cadena.strip()         # "Hola Mundo" (quita espacios al inicio y final)
cadena.lstrip()        # "Hola Mundo  " (quita espacios a la izquierda)
cadena.rstrip()        # "  Hola Mundo" (quita espacios a la derecha)

# Reemplazar
cadena.replace('Mundo', 'Python')  # "  Hola Python  "
```

### Métodos de división y unión

```python
cadena = "Hola Mundo Python"

# Dividir en lista
palabras = cadena.split()           # ['Hola', 'Mundo', 'Python']
partes = cadena.split('o')          # ['H', 'la Mund', ' Pyth', 'n']

# Unir lista en cadena
lista = ['Hola', 'Mundo', 'Python']
unida = ' '.join(lista)             # "Hola Mundo Python"
separador = '-'.join(lista)         # "Hola-Mundo-Python"
```

### Métodos de búsqueda

```python
cadena = "programacion en python"

# Buscar posición
pos = cadena.find('python')         # 16 (posición donde empieza)
pos = cadena.find('java')           # -1 (no encontrado)

# index() es igual pero lanza excepción si no encuentra
pos = cadena.index('python')        # 16

# Contar ocurrencias
veces = cadena.count('o')           # 2
```

### Métodos de verificación (devuelven booleanos)

```python
cadena = "programacion en python"

# Comprobar inicio y final
cadena.startswith('pro')            # True
cadena.endswith('on')               # True

# Verificar contenido
"123".isdigit()                     # True (solo dígitos)
"abc".isalpha()                     # True (solo letras)
"abc123".isalnum()                  # True (letras y números)
"   ".isspace()                     # True (solo espacios)
"Hola".islower()                    # False
"HOLA".isupper()                    # True
```

## 🔹 9. UNICODE Y ASCII

### Códigos de caracteres

```python
# Obtener código Unicode de un carácter
emoji = '😄'
codigo = ord(emoji)                 # 128516
codigo_hex = hex(ord(emoji))        # '0x1f604'

# Crear carácter desde código
caracter = chr(9731)                # '☃' (muñeco de nieve)
caracter = chr(65)                  # 'A'

# Generar rango de caracteres ASCII
digitos = ''.join(chr(i) for i in range(48, 58))  # "0123456789"
letras = ''.join(chr(i) for i in range(65, 91))   # "ABC...XYZ"
```

## 🔹 10. RESUMEN OPERADORES Y MÉTODOS

| Operación       | Sintaxis     | Ejemplo                    | Resultado         |
| --------------- | ------------ | -------------------------- | ----------------- |
| Concatenar      | `+`          | `"Hola" + " " + "Mundo"`   | `"Hola Mundo"`    |
| Repetir         | `*`          | `"Ha" * 3`                 | `"HaHaHa"`        |
| Acceso          | `[i]`        | `"Python"[0]`              | `"P"`             |
| Slicing         | `[i:j:k]`    | `"Python"[1:4]`            | `"yth"`           |
| Pertenencia     | `in`         | `"la" in "Hola"`           | `True`            |
| Longitud        | `len()`      | `len("Hola")`              | `4`               |
| Mayúsculas      | `.upper()`   | `"hola".upper()`           | `"HOLA"`          |
| Minúsculas      | `.lower()`   | `"HOLA".lower()`           | `"hola"`          |
| Dividir         | `.split()`   | `"a b c".split()`          | `['a', 'b', 'c']` |
| Unir            | `.join()`    | `"-".join(['a', 'b'])`     | `"a-b"`           |
| Reemplazar      | `.replace()` | `"Hola".replace('o', 'a')` | `"Hala"`          |
| Buscar          | `.find()`    | `"Hola".find('la')`        | `2`               |
| Contar          | `.count()`   | `"Hola".count('o')`        | `1`               |
| Quitar espacios | `.strip()`   | `"  hi  ".strip()`         | `"hi"`            |

---

# UNIDAD 5: FICHEROS CSV Y JSON

## 🔹 1. FICHEROS CSV

### ¿Qué es CSV?

- **CSV** = Comma-Separated Values (Valores Separados por Comas)
- Formato de texto plano para almacenar datos tabulares
- Cada línea es un registro, los valores se separan por comas (o punto y coma)

### Estructura básica

```csv
Ciudad,País,Población (millones)
Madrid,España,3.2
París,Francia,2.1
Londres,Reino Unido,9.0
```

### 1.1. LECTURA DE CSV con reader

```python
from csv import reader

try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector_csv = reader(archivo)

        # Saltar la primera línea (cabecera)
        next(lector_csv, None)

        # Leer cada fila
        for fila in lector_csv:
            print(f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo no existe.")
except PermissionError:
    print("Error: No se tiene permiso para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

**Características:**

- `reader()` lee el CSV como lista de listas
- Cada fila es una lista de strings
- Se accede a los valores por índice: `fila[0]`, `fila[1]`, etc.

### 1.2. LECTURA DE CSV con DictReader

```python
from csv import DictReader

try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        campos = ["Ciudad", "País", "Población (millones)"]

        # Leer primera línea
        primera_linea = archivo.readline().strip()

        # Reiniciar lectura SIEMPRE
        archivo.seek(0)

        # Detectar si tiene cabecera
        if primera_linea.split(",") == campos:
            # Tiene cabecera
            lector = DictReader(archivo)
            print("Nombres de las columnas:", lector.fieldnames)
        else:
            # No tiene cabecera → se la asignamos manualmente
            lector = DictReader(archivo, fieldnames=campos)
            print("Nombres de las columnas (asignadas):", campos)

        # Leer cada fila como diccionario
        for fila in lector:
            print(f"{fila['Ciudad']} ({fila['País']}) tiene {fila['Población (millones)']} millones.")

except FileNotFoundError:
    print("Error: El archivo no existe.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

**Características:**

- `DictReader()` lee el CSV como lista de diccionarios
- Se accede a los valores por nombre de columna: `fila['Ciudad']`
- Más legible y menos propenso a errores
- `archivo.seek(0)` reinicia el puntero al inicio del archivo

### 1.3. ESCRITURA DE CSV con writer

```python
from csv import writer

capitales = [
    ["Ciudad", "País", "Continente"],
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"],
]

try:
    with open("capitales.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = writer(archivo_csv)

        # Escribir cabecera
        escritor_csv.writerow(capitales[0])

        # Escribir datos
        escritor_csv.writerows(capitales[1:])

except OSError as e:
    print(f"Error de E/S: {e.strerror}")
else:
    print("Archivo 'capitales.csv' creado correctamente.")
```

**Características:**

- `writer()` escribe listas en formato CSV
- `writerow()` escribe una fila
- `writerows()` escribe múltiples filas
- **IMPORTANTE:** usar `newline=""` para evitar líneas en blanco adicionales

### 1.4. ESCRITURA DE CSV con DictWriter

```python
from csv import DictWriter

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"},
]

try:
    with open("patrimonios.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        fieldnames = ["Ciudad", "País", "Lugar emblemático"]
        escritor_csv = DictWriter(archivo_csv, fieldnames=fieldnames, delimiter=";")

        # Escribir cabecera
        escritor_csv.writeheader()

        # Escribir datos
        escritor_csv.writerows(patrimonios)

except OSError as e:
    print(f"Error de E/S: {e.strerror}")
else:
    print("Archivo 'patrimonios.csv' generado correctamente.")
```

**Características:**

- `DictWriter()` escribe diccionarios en formato CSV
- `writeheader()` escribe la cabecera automáticamente
- `delimiter` permite cambiar el separador (`;` en lugar de `,`)

### Resumen CSV

| Operación              | Clase        | Uso                                          |
| ---------------------- | ------------ | -------------------------------------------- |
| Leer como listas       | `reader`     | Cuando no importan los nombres de columnas   |
| Leer como diccionarios | `DictReader` | Cuando quieres acceder por nombre de columna |
| Escribir listas        | `writer`     | Para escribir datos como listas              |
| Escribir diccionarios  | `DictWriter` | Para escribir datos como diccionarios        |

**Parámetros importantes:**

- `encoding="utf-8"`: para caracteres especiales (ñ, acentos, etc.)
- `newline=""`: evita líneas en blanco al escribir
- `delimiter`: para cambiar el separador (`,`, `;`, `\t`, etc.)

---

## 🔹 2. FICHEROS JSON

### ¿Qué es JSON?

- **JSON** = JavaScript Object Notation
- Formato de texto para intercambio de datos
- Similar a diccionarios de Python
- Soporta: strings, números, booleanos, listas, diccionarios, null

### Estructura básica

```json
{
  "nombre": "Francia",
  "capital": "París",
  "poblacion": 67,
  "idiomas": ["Francés"],
  "es_europeo": true
}
```

### 2.1. LECTURA DE JSON con json.load()

```python
import json

try:
    with open("paises.json", "r", encoding="utf-8") as archivo:
        paises = json.load(archivo)  # Lee archivo y convierte a objeto Python

        for pais in paises:
            print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo 'paises.json' no se encuentra.")
except json.JSONDecodeError:
    print("Error: El archivo contiene un JSON inválido.")
except Exception as e:
    print("Ocurrió un error:", e)
```

**Características:**

- `json.load()` lee un archivo JSON y lo convierte a objeto Python
- Convierte automáticamente:
  - Objeto JSON → diccionario Python
  - Array JSON → lista Python
  - String → str
  - Number → int o float
  - true/false → True/False
  - null → None

### 2.2. ESCRITURA DE JSON con json.dump()

```python
import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"},
]

try:
    with open("capitales.json", "w", encoding="utf-8") as archivo:
        json.dump(capitales, archivo, ensure_ascii=False, indent=4)

    print("Archivo 'capitales.json' creado correctamente.")

except Exception as e:
    print("Ocurrió un error al crear el archivo:", e)
```

**Características:**

- `json.dump()` escribe un objeto Python en un archivo JSON
- **Parámetros importantes:**
  - `ensure_ascii=False`: permite caracteres UTF-8 (acentos, ñ, etc.)
  - `indent=4`: formatea con espacios para mejor legibilidad
  - `sort_keys=True`: ordena las claves alfabéticamente

### 2.3. CONVERSIÓN DESDE CADENA con json.loads()

```python
import json

cadena_json = """
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
"""

try:
    paises = json.loads(cadena_json)  # Convierte string JSON a objeto Python

    print("Tipo de dato obtenido:", type(paises))

    for pais in paises:
        print(f"{pais['nombre']} usa la moneda {pais['moneda']}.")

except json.JSONDecodeError:
    print("Error: La cadena JSON no es válida.")
except Exception as e:
    print("Ocurrió un error:", e)
```

**Nota:** `json.loads()` con **s** (string) convierte una cadena JSON a objeto Python.

### 2.4. CONVERSIÓN A CADENA con json.dumps()

```python
import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000,
}

# Convierte objeto Python a cadena JSON
cadena_json = json.dumps(pais, indent=2, sort_keys=True)
print(cadena_json)
```

**Nota:** `json.dumps()` con **s** (string) convierte un objeto Python a cadena JSON.

### 2.5. EJEMPLO COMPLETO: Filtrar y guardar

```python
import json

try:
    # Leer archivo JSON
    with open("paises.json", "r", encoding="utf-8") as f:
        paises = json.load(f)

    # Pedir continente al usuario
    continente = input("Introduce un continente: ").strip()

    # Filtrar países
    filtrados = []
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            filtrados.append(pais)

    # Mostrar resultados
    if filtrados:
        print("\nPaíses encontrados:")
        for p in filtrados:
            print(f"- {p['nombre']} ({p['poblacion']} millones)")
    else:
        print("No se encontraron países en ese continente.")

    # Guardar resultados en nuevo archivo
    with open("paises_filtrados.json", "w", encoding="utf-8") as f:
        json.dump(filtrados, f, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except (FileNotFoundError, json.JSONDecodeError) as e:
    print("Error con el archivo JSON:", e)
except Exception as e:
    print("Error inesperado:", e)
```

### Resumen JSON

| Función        | Descripción                    | Entrada       | Salida        |
| -------------- | ------------------------------ | ------------- | ------------- |
| `json.load()`  | Lee archivo JSON               | Archivo       | Objeto Python |
| `json.dump()`  | Escribe objeto en archivo JSON | Objeto Python | Archivo       |
| `json.loads()` | Convierte cadena JSON          | String JSON   | Objeto Python |
| `json.dumps()` | Convierte objeto a cadena JSON | Objeto Python | String JSON   |

**Parámetros importantes:**

- `ensure_ascii=False`: permite UTF-8 (ñ, acentos)
- `indent=4`: formatea con espacios
- `sort_keys=True`: ordena las claves

### Comparación CSV vs JSON

| Aspecto        | CSV                                | JSON                                                  |
| -------------- | ---------------------------------- | ----------------------------------------------------- |
| Estructura     | Tabular (filas y columnas)         | Jerárquica (anidada)                                  |
| Tipos de datos | Solo texto                         | Múltiples (string, number, bool, null, array, object) |
| Legibilidad    | Alta en Excel/hoja de cálculo      | Alta para programadores                               |
| Tamaño         | Más compacto                       | Más verboso                                           |
| Uso típico     | Datos tabulares, exportación Excel | APIs, configuraciones, datos complejos                |

---

# UNIDAD 6: PROGRAMACIÓN ORIENTADA A OBJETOS

## 🔹 1. CONCEPTOS BÁSICOS

### ¿Qué es POO?

- **POO** = Programación Orientada a Objetos
- Paradigma de programación basado en "objetos"
- **Objeto**: entidad que combina datos (atributos) y comportamiento (métodos)
- **Clase**: plantilla o molde para crear objetos

### Ventajas de POO

- ✅ Reutilización de código
- ✅ Organización y estructura
- ✅ Encapsulación (ocultar detalles internos)
- ✅ Herencia (compartir características)
- ✅ Polimorfismo (mismo método, diferentes comportamientos)

---

## 🔹 2. CLASES Y OBJETOS

### Definición básica de una clase

```python
class Animal:
    # Constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre      # Atributo público
        self.especie = especie
        self.edad = edad

    # Método
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad = self.edad + 1

# Crear objetos (instancias)
animal1 = Animal("Toby", "Perro", 4)
animal2 = Animal("Miau", "Gato", 2)

# Usar métodos
animal1.saludar()  # "Soy un Perro llamado Toby y tengo 4 años."
animal1.cumplir_anios()
print(animal1.edad)  # 5
```

**Conceptos clave:**

- `class`: define una clase
- `__init__`: constructor, se ejecuta al crear objeto
- `self`: referencia al objeto actual (como `this` en otros lenguajes)
- Los métodos siempre llevan `self` como primer parámetro

---

## 🔹 3. ATRIBUTOS

### Tipos de atributos

#### Atributos de instancia (públicos)

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad

persona = Persona("Ana", 25)
print(persona.nombre)  # Acceso directo
persona.edad = 26      # Modificación directa
```

#### Atributos privados (convención con \_\_)

```python
class Animal:
    def __init__(self, nombre, id_chip):
        self.nombre = nombre
        self.__id_chip = id_chip  # Atributo privado (name mangling)

    def mostrar_chip(self):
        print(f"ID Chip: {self.__id_chip}")

animal = Animal("Rex", "ABC123")
# animal.__id_chip  # ❌ Error: no se puede acceder directamente
animal.mostrar_chip()  # ✅ Acceso a través de método
```

**Nota:** En Python, `__atributo` no es realmente privado, pero se "oculta" mediante name mangling (`_NombreClase__atributo`).

#### Atributos de clase (compartidos por todas las instancias)

```python
class Animal:
    __numero_animales = 0  # Atributo de clase privado

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.__numero_animales += 1

    @classmethod
    def numero_animales(cls):
        return cls.__numero_animales

animal1 = Animal("Rex")
animal2 = Animal("Miau")
print(Animal.numero_animales())  # 2
```

---

## 🔹 4. PROPIEDADES (GETTERS Y SETTERS)

### ¿Por qué usar propiedades?

- Controlar el acceso a atributos privados
- Validar valores antes de asignarlos
- Ejecutar lógica adicional al leer/escribir

### Sintaxis con @property

```python
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.__peso = peso  # Atributo privado

    # Getter
    @property
    def peso(self):
        return self.__peso

    # Setter
    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso > 0:
            print("Se ha cambiado el peso")
            self.__peso = nuevo_peso
        else:
            raise Exception("El peso debe ser mayor que 0")

# Uso como si fuera un atributo normal
animal = Animal("Rex", 10)
print(animal.peso)    # Llama al getter → 10
animal.peso = 15      # Llama al setter → "Se ha cambiado el peso"
print(animal.peso)    # 15
# animal.peso = -5    # ❌ Excepción: "El peso debe ser mayor que 0"
```

**Ventajas:**

- Sintaxis limpia (acceso como atributo)
- Validación automática
- Encapsulación (el atributo real está oculto)

---

## 🔹 5. MÉTODOS

### Tipos de métodos

#### Métodos de instancia (normales)

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):  # Método de instancia
        print(f"Hola, soy {self.nombre}")

animal = Animal("Rex")
animal.saludar()  # "Hola, soy Rex"
```

#### Métodos de clase (@classmethod)

```python
class Animal:
    __numero_animales = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.__numero_animales += 1

    @classmethod
    def numero_animales(cls):  # Método de clase
        return cls.__numero_animales

print(Animal.numero_animales())  # Se llama sin instancia
```

**Características:**

- Se llaman sobre la clase, no sobre instancias
- Primer parámetro es `cls` (referencia a la clase)
- Útiles para contadores, fábricas, etc.

#### Métodos estáticos (@staticmethod)

```python
class Animal:
    @staticmethod
    def es_mayor_de_edad(edad):  # Método estático
        return edad >= 2

# Se llama sin instancia
if Animal.es_mayor_de_edad(3):
    print("Es mayor de edad")
```

**Características:**

- No reciben `self` ni `cls`
- No acceden a atributos de instancia ni de clase
- Son funciones "de utilidad" relacionadas con la clase

### Resumen de métodos

| Tipo      | Decorador       | Primer parámetro | Acceso a               | Llamada           |
| --------- | --------------- | ---------------- | ---------------------- | ----------------- |
| Instancia | Ninguno         | `self`           | Atributos de instancia | `objeto.metodo()` |
| Clase     | `@classmethod`  | `cls`            | Atributos de clase     | `Clase.metodo()`  |
| Estático  | `@staticmethod` | Ninguno          | Nada de la clase       | `Clase.metodo()`  |

---

## 🔹 6. HERENCIA

### ¿Qué es la herencia?

- Crear clases nuevas basadas en clases existentes
- La clase hija (derivada) hereda atributos y métodos de la clase padre (base)
- Permite reutilizar código y establecer jerarquías

### Sintaxis básica

```python
# Clase padre (base)
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

    def saludar(self):
        print(f"Soy un animal llamado {self.nombre}, tengo {self.edad} años y peso {self.peso} kilos.")

# Clase hija
class Mamifero(AnimalTerrestre):  # Hereda de AnimalTerrestre
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)  # Llamar al constructor del padre
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

    # Sobrescribir método (polimorfismo)
    def saludar(self):
        print(f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años y mi gestación es de {self.gestacion_dias} días.")

# Usar clases
animal = AnimalTerrestre("Rex", 5, 20)
animal.saludar()  # "Soy un animal llamado Rex, tengo 5 años y peso 20 kilos."

mamifero = Mamifero("Luna", 3, 15, 60)
mamifero.saludar()  # "Soy un mamífero llamado Luna, tengo 3 años y mi gestación es de 60 días."
```

### Conceptos clave

#### super()

- Llama a métodos de la clase padre
- Usado principalmente en `__init__` para inicializar atributos del padre

```python
class Hijo(Padre):
    def __init__(self, param1, param2, param3):
        super().__init__(param1, param2)  # Inicializa atributos del padre
        self.param3 = param3
```

#### Sobrescritura de métodos (Override)

- La clase hija puede redefinir métodos del padre
- Se usa para cambiar el comportamiento

```python
class Padre:
    def saludar(self):
        print("Hola desde Padre")

class Hijo(Padre):
    def saludar(self):  # Sobrescribe el método
        print("Hola desde Hijo")

hijo = Hijo()
hijo.saludar()  # "Hola desde Hijo"
```

### Ejemplo completo con múltiples clases hijas

```python
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

    def saludar(self):
        print(f"Soy un animal llamado {self.nombre}")

class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias

    @property
    def gestacion_dias(self):
        return self.__gestacion_dias

    def saludar(self):
        print(f"Soy un mamífero llamado {self.nombre}, gestación de {self.gestacion_dias} días.")

class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    def saludar(self):
        volar_texto = "Puedo volar" if self.puede_volar else "No puedo volar"
        print(f"Soy un ave llamado {self.nombre}. {volar_texto}.")

# Crear instancias
animal = AnimalTerrestre("Rex", 5, 20)
mamifero = Mamifero("Luna", 3, 15, 60)
ave = Ave("Piolín", 1, 0.5, True)

# Polimorfismo: cada uno ejecuta su propia versión de saludar()
animal.saludar()
mamifero.saludar()
ave.saludar()
```

---

## 🔹 7. DECORADORES

### ¿Qué son los decoradores?

- Funciones que modifican el comportamiento de otras funciones
- Se aplican con la sintaxis `@nombre_decorador`
- Útiles para añadir funcionalidad sin modificar la función original

### Sintaxis básica

```python
def decorador(funcion):
    def envoltura():
        print("Estoy antes")
        funcion()
        print("Estoy después")
    return envoltura

@decorador
def mi_funcion():
    print("Estoy dentro")

mi_funcion()
# Salida:
# Estoy antes
# Estoy dentro
# Estoy después
```

**Explicación:**

1. `@decorador` es equivalente a `mi_funcion = decorador(mi_funcion)`
2. Cuando se llama `mi_funcion()`, se ejecuta `envoltura()`
3. `envoltura()` ejecuta código antes, durante y después de la función original

### Decoradores comunes en Python

| Decorador          | Uso                                   |
| ------------------ | ------------------------------------- |
| `@property`        | Convierte método en atributo (getter) |
| `@atributo.setter` | Define setter para propiedad          |
| `@classmethod`     | Define método de clase                |
| `@staticmethod`    | Define método estático                |

---

## 🔹 8. MANEJO DE EXCEPCIONES

### Try-Except en POO

```python
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso <= 0:
            raise Exception("El peso debe ser mayor que 0")
        self.__peso = nuevo_peso

try:
    animal = Animal("Rex", 10)
    print(animal.peso)  # 10

    animal.peso = -5    # Lanza excepción

except Exception as e:
    print(f"Error: {e}")  # "Error: El peso debe ser mayor que 0"
```

### ValueError en validaciones

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = nueva_edad

try:
    persona = Persona("Ana", 25)
    persona.edad = -5
except ValueError as e:
    print(f"Error: {e}")
```

---

## 🔹 9. EJEMPLO COMPLETO INTEGRADO

```python
class Animal:
    # Atributo de clase (compartido)
    __numero_animales = 0

    def __init__(self, nombre, especie, edad, id_chip, peso=60):
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip  # Privado
        self.__peso = peso        # Privado
        Animal.__numero_animales += 1

    # Property: getter
    @property
    def id_chip(self):
        return self.__id_chip

    # Property: setter con validación
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

    # Método de clase
    @classmethod
    def numero_animales(cls):
        return cls.__numero_animales

    # Método estático
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 2

    # Métodos de instancia
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad = self.edad + 1

# Uso
try:
    animal1 = Animal("Juanito", "Perro", 4, "ejemplo1", 10)
    animal2 = Animal("Pepe", "Gato", 2, "ejemplo2", 5)

    print(Animal.numero_animales())  # 2

    print(animal1.id_chip)           # ejemplo1
    animal1.id_chip = "nuevo_chip"   # "Se ha cambiado el id_chip"

    print(animal2.peso)              # 5
    animal2.peso = 10                # "Se ha cambiado el peso"

    if Animal.es_mayor_de_edad(3):
        print("Es mayor de edad")

except Exception as e:
    print(e)
```

---

## 🔹 10. RESUMEN POO

### Conceptos clave

| Concepto          | Descripción                            | Ejemplo               |
| ----------------- | -------------------------------------- | --------------------- |
| **Clase**         | Plantilla para crear objetos           | `class Animal:`       |
| **Objeto**        | Instancia de una clase                 | `animal = Animal()`   |
| **Atributo**      | Variable asociada a objeto/clase       | `self.nombre`         |
| **Método**        | Función asociada a objeto/clase        | `def saludar(self):`  |
| **Constructor**   | Método especial para inicializar       | `def __init__(self):` |
| **Encapsulación** | Ocultar atributos con `__`             | `self.__peso`         |
| **Property**      | Getter/Setter con sintaxis limpia      | `@property`           |
| **Herencia**      | Clase hija hereda de padre             | `class Hijo(Padre):`  |
| **Polimorfismo**  | Mismo método, diferente comportamiento | Sobrescribir métodos  |
| **Decorador**     | Modifica comportamiento de funciones   | `@decorador`          |

### Tipos de métodos

```python
class MiClase:
    # Método de instancia
    def metodo_instancia(self):
        pass

    # Método de clase
    @classmethod
    def metodo_clase(cls):
        pass

    # Método estático
    @staticmethod
    def metodo_estatico():
        pass
```

### Visibilidad de atributos

```python
class MiClase:
    def __init__(self):
        self.publico = "accesible"
        self._protegido = "por convención"  # Convención: no usar fuera
        self.__privado = "name mangling"    # No accesible directamente
```

---

## 📝 CONSEJOS PARA EL EXAMEN

### UNIDAD 4 (Cadenas)

✅ Memoriza métodos principales: `upper()`, `lower()`, `split()`, `join()`, `replace()`, `strip()`  
✅ Recuerda slicing: `[inicio:fin:paso]` y que `-1` invierte  
✅ Practica f-strings: `f"Hola {variable}"`  
✅ Conoce `ord()` y `chr()` para Unicode  
✅ Diferencia entre `find()` (retorna -1) e `index()` (lanza excepción)

### UNIDAD 5 (Ficheros)

✅ **CSV**: diferencia entre `reader`/`writer` (listas) y `DictReader`/`DictWriter` (diccionarios)  
✅ **CSV**: recuerda `newline=""` al escribir  
✅ **CSV**: `next(lector)` para saltar cabecera  
✅ **CSV**: `archivo.seek(0)` para reiniciar lectura  
✅ **JSON**: diferencia entre `load`/`dump` (archivos) y `loads`/`dumps` (strings)  
✅ **JSON**: usa `ensure_ascii=False` e `indent=4`  
✅ Usa bloques `try-except` para manejar errores

### UNIDAD 6 (POO)

✅ Constructor siempre es `__init__(self, ...)`  
✅ Atributos privados con `__nombre`  
✅ Properties: `@property` para getter, `@nombre.setter` para setter  
✅ Herencia: usa `super().__init__()` en constructor de clase hija  
✅ Tres tipos de métodos: instancia (`self`), clase (`@classmethod`, `cls`), estático (`@staticmethod`)  
✅ Decoradores: función que envuelve otra función  
✅ Validaciones en setters con `raise Exception()` o `raise ValueError()`

---

## 🎯 PATRONES COMUNES

### Leer CSV y procesar

```python
from csv import DictReader

with open("datos.csv", "r", encoding="utf-8") as f:
    lector = DictReader(f)
    for fila in lector:
        # Procesar cada fila
        print(fila['columna'])
```

### Escribir JSON

```python
import json

datos = [{"nombre": "Ana", "edad": 25}]

with open("salida.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)
```

### Clase con property

```python
class MiClase:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__valor = nuevo_valor
        else:
            raise ValueError("Debe ser positivo")
```

### Herencia básica

```python
class Padre:
    def __init__(self, param1):
        self.param1 = param1

class Hijo(Padre):
    def __init__(self, param1, param2):
        super().__init__(param1)
        self.param2 = param2
```

---

**¡Buena suerte en tu examen! 🚀**
