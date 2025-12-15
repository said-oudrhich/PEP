"""
═══════════════════════════════════════════════════════════════════════════
GUÍA COMPLETA: FICHEROS JSON EN PYTHON
═══════════════════════════════════════════════════════════════════════════

Este archivo contiene TODOS los ejemplos y operaciones con archivos JSON que 
necesitas para el examen. Usa Ctrl+F para buscar rápidamente lo que necesites.

ÍNDICE RÁPIDO (busca estos títulos):
1. LECTURA DE JSON (json.load desde archivo)
2. ESCRITURA DE JSON (json.dump a archivo)
3. CONVERSIÓN DESDE CADENAS (json.loads)
4. CONVERSIÓN A CADENAS (json.dumps)
5. TIPOS DE DATOS PYTHON ↔ JSON
6. FORMATEO Y PRETTY-PRINTING
7. MANEJO DE ERRORES
8. JSON ANIDADO (nested)
9. EJERCICIOS PRÁCTICOS COMPLETOS

═══════════════════════════════════════════════════════════════════════════
"""

import json

# ═══════════════════════════════════════════════════════════════════════════
# 1. LECTURA DE JSON - json.load()
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("1. LECTURA DE JSON - json.load()")
print("=" * 80)

# EJEMPLO 1: Lectura básica
print("\n--- EJEMPLO 1: Lectura básica de JSON ---")

# Crear archivo de prueba
paises_data = [
    {"nombre": "España", "continente": "Europa", "poblacion": 47},
    {"nombre": "México", "continente": "América", "poblacion": 126},
    {"nombre": "Japón", "continente": "Asia", "poblacion": 126}
]

with open("paises.json", "w", encoding="utf-8") as f:
    json.dump(paises_data, f, ensure_ascii=False, indent=2)

try:
    with open("paises.json", "r", encoding="utf-8") as archivo:
        paises = json.load(archivo)
        
        print(f"Tipo de dato: {type(paises)}")
        print(f"Número de países: {len(paises)}")
        
        for pais in paises:
            print(f"  {pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("⚠ Error: El archivo 'paises.json' no se encuentra.")
except json.JSONDecodeError:
    print("⚠ Error: El archivo contiene un JSON inválido.")
except Exception as e:
    print(f"⚠ Ocurrió un error: {e}")

# EJEMPLO 2: Lectura de JSON con diccionario
print("\n--- EJEMPLO 2: JSON como diccionario ---")

usuario_data = {
    "nombre": "Ana García",
    "edad": 28,
    "email": "ana@example.com",
    "activo": True,
    "pais": "España"
}

with open("usuario.json", "w", encoding="utf-8") as f:
    json.dump(usuario_data, f, ensure_ascii=False, indent=2)

try:
    with open("usuario.json", "r", encoding="utf-8") as archivo:
        usuario = json.load(archivo)
        
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Email: {usuario['email']}")
        print(f"Activo: {usuario['activo']}")

except FileNotFoundError:
    print("⚠ El archivo no existe.")
except json.JSONDecodeError as e:
    print(f"⚠ JSON inválido: {e}")

# EJEMPLO 3: Acceder a datos anidados
print("\n--- EJEMPLO 3: JSON anidado ---")

persona_data = {
    "nombre": "Carlos López",
    "edad": 35,
    "direccion": {
        "calle": "Gran Vía 28",
        "ciudad": "Madrid",
        "codigo_postal": "28013"
    },
    "telefonos": [
        "+34 600 123 456",
        "+34 910 987 654"
    ]
}

with open("persona.json", "w", encoding="utf-8") as f:
    json.dump(persona_data, f, ensure_ascii=False, indent=2)

try:
    with open("persona.json", "r", encoding="utf-8") as archivo:
        persona = json.load(archivo)
        
        print(f"Nombre: {persona['nombre']}")
        print(f"Ciudad: {persona['direccion']['ciudad']}")
        print(f"Primera teléfono: {persona['telefonos'][0]}")

except Exception as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 2. ESCRITURA DE JSON - json.dump()
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("2. ESCRITURA DE JSON - json.dump()")
print("=" * 80)

# EJEMPLO 1: Escribir lista de diccionarios
print("\n--- EJEMPLO 1: Escribir lista de diccionarios ---")

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"},
]

try:
    with open("capitales.json", "w", encoding="utf-8") as archivo:
        json.dump(capitales, archivo, ensure_ascii=False, indent=4)
    
    print("✓ Archivo 'capitales.json' creado correctamente.")
    
except Exception as e:
    print(f"⚠ Ocurrió un error al crear el archivo: {e}")

# EJEMPLO 2: Escribir diccionario complejo
print("\n--- EJEMPLO 2: Escribir diccionario complejo ---")

producto = {
    "id": 101,
    "nombre": "Laptop HP",
    "precio": 899.99,
    "en_stock": True,
    "categorias": ["Electrónica", "Informática"],
    "especificaciones": {
        "procesador": "Intel i7",
        "ram": "16GB",
        "almacenamiento": "512GB SSD"
    }
}

try:
    with open("producto.json", "w", encoding="utf-8") as archivo:
        json.dump(producto, archivo, ensure_ascii=False, indent=2)
    
    print("✓ Archivo 'producto.json' creado.")
    
except Exception as e:
    print(f"⚠ Error: {e}")

# EJEMPLO 3: Escribir sin formateo (compacto)
print("\n--- EJEMPLO 3: JSON compacto (sin indentación) ---")

datos_compactos = {"nombre": "Test", "valor": 42, "activo": True}

try:
    with open("compacto.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_compactos, archivo, ensure_ascii=False)
    
    print("✓ Archivo compacto creado.")
    
    # Leer y mostrar contenido
    with open("compacto.json", "r", encoding="utf-8") as f:
        contenido = f.read()
        print(f"Contenido: {contenido}")
    
except Exception as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 3. CONVERSIÓN DESDE CADENAS - json.loads()
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("3. CONVERSIÓN DESDE CADENAS - json.loads()")
print("=" * 80)

# EJEMPLO 1: Convertir cadena JSON a objeto Python
print("\n--- EJEMPLO 1: json.loads() básico ---")

cadena_json = """
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
"""

try:
    paises = json.loads(cadena_json)
    print(f"Tipo de dato obtenido: {type(paises)}")
    
    for pais in paises:
        print(f"  {pais['nombre']} usa la moneda {pais['moneda']}.")

except json.JSONDecodeError:
    print("⚠ Error: La cadena JSON no es válida.")
except Exception as e:
    print(f"⚠ Ocurrió un error: {e}")

# EJEMPLO 2: Convertir diferentes tipos
print("\n--- EJEMPLO 2: Conversión de diferentes tipos ---")

print("Lista:", json.loads('[1, 2, 3, 4, 5]'))
print("Diccionario:", json.loads('{"nombre": "Ana", "edad": 25}'))
print("Cadena:", json.loads('"Hola Mundo"'))
print("Número:", json.loads('42'))
print("Booleano:", json.loads('true'))
print("Null:", json.loads('null'))

# EJEMPLO 3: Parsear respuesta API simulada
print("\n--- EJEMPLO 3: Simular respuesta de API ---")

respuesta_api = """{
    "status": "success",
    "data": {
        "id": 123,
        "username": "user_demo",
        "email": "demo@example.com"
    },
    "timestamp": "2024-01-15T10:30:00Z"
}"""

try:
    datos = json.loads(respuesta_api)
    
    if datos['status'] == 'success':
        print("✓ Petición exitosa")
        print(f"  Usuario: {datos['data']['username']}")
        print(f"  Email: {datos['data']['email']}")
    
except json.JSONDecodeError as e:
    print(f"⚠ JSON inválido: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 4. CONVERSIÓN A CADENAS - json.dumps()
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("4. CONVERSIÓN A CADENAS - json.dumps()")
print("=" * 80)

# EJEMPLO 1: Convertir diccionario a cadena JSON
print("\n--- EJEMPLO 1: json.dumps() básico ---")

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000,
}

cadena_json = json.dumps(pais, indent=2, sort_keys=True)
print(cadena_json)

# EJEMPLO 2: Diferentes opciones de formateo
print("\n--- EJEMPLO 2: Opciones de formateo ---")

datos = {"nombre": "Python", "versión": 3.11, "gratis": True}

print("Sin formateo:")
print(json.dumps(datos))

print("\nCon indentación de 2 espacios:")
print(json.dumps(datos, indent=2))

print("\nCon indentación de 4 espacios:")
print(json.dumps(datos, indent=4))

print("\nCon claves ordenadas:")
print(json.dumps(datos, indent=2, sort_keys=True))

print("\nCon ensure_ascii=False (permite caracteres Unicode):")
texto_unicode = {"mensaje": "Hola, España 🇪🇸"}
print(json.dumps(texto_unicode, ensure_ascii=False))

# EJEMPLO 3: Separadores personalizados
print("\n--- EJEMPLO 3: Separadores personalizados ---")

datos = {"a": 1, "b": 2, "c": 3}

print("Compacto (sin espacios):")
print(json.dumps(datos, separators=(',', ':')))

print("\nCon espacios:")
print(json.dumps(datos, separators=(', ', ': ')))

print()

# ═══════════════════════════════════════════════════════════════════════════
# 5. TIPOS DE DATOS PYTHON ↔ JSON
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("5. TIPOS DE DATOS PYTHON ↔ JSON")
print("=" * 80)

print("""
CONVERSIÓN AUTOMÁTICA PYTHON → JSON:
────────────────────────────────────────
  Python          →    JSON
────────────────────────────────────────
  dict            →    object
  list, tuple     →    array
  str             →    string
  int, float      →    number
  True            →    true
  False           →    false
  None            →    null
────────────────────────────────────────

CONVERSIÓN AUTOMÁTICA JSON → PYTHON:
────────────────────────────────────────
  JSON            →    Python
────────────────────────────────────────
  object          →    dict
  array           →    list
  string          →    str
  number (int)    →    int
  number (float)  →    float
  true            →    True
  false           →    False
  null            →    None
────────────────────────────────────────
""")

# Ejemplo práctico
print("--- EJEMPLO práctico de conversiones ---\n")

datos_python = {
    "texto": "Hola",
    "numero_entero": 42,
    "numero_decimal": 3.14,
    "booleano_true": True,
    "booleano_false": False,
    "nulo": None,
    "lista": [1, 2, 3],
    "tupla": (4, 5, 6),  # Se convierte a array en JSON
    "diccionario": {"clave": "valor"}
}

json_string = json.dumps(datos_python, indent=2)
print("Python → JSON:")
print(json_string)

print("\nJSON → Python:")
datos_recuperados = json.loads(json_string)
for clave, valor in datos_recuperados.items():
    print(f"  {clave}: {valor} (tipo: {type(valor).__name__})")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 6. FORMATEO Y PRETTY-PRINTING
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("6. FORMATEO Y PRETTY-PRINTING")
print("=" * 80)

datos_ejemplo = {
    "usuarios": [
        {"id": 1, "nombre": "Ana", "email": "ana@example.com"},
        {"id": 2, "nombre": "Luis", "email": "luis@example.com"}
    ],
    "total": 2,
    "página": 1
}

print("\n--- OPCIONES DE FORMATEO ---\n")

print("1. Sin formateo (una línea):")
print(json.dumps(datos_ejemplo))

print("\n2. Con indent=2:")
print(json.dumps(datos_ejemplo, indent=2))

print("\n3. Con indent=4 y sort_keys=True:")
print(json.dumps(datos_ejemplo, indent=4, sort_keys=True))

print("\n4. Compacto (sin espacios):")
print(json.dumps(datos_ejemplo, separators=(',', ':')))

print("\n5. Con ensure_ascii=False (caracteres especiales):")
datos_unicode = {"mensaje": "España, México, Perú 🌍"}
print(json.dumps(datos_unicode, ensure_ascii=False, indent=2))

print()

# ═══════════════════════════════════════════════════════════════════════════
# 7. MANEJO DE ERRORES
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("7. MANEJO DE ERRORES")
print("=" * 80)

print("\n--- PLANTILLA COMPLETA de manejo de errores ---\n")

print("""
# LECTURA DE ARCHIVO JSON:
try:
    with open("archivo.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        # Procesar datos...
        
except FileNotFoundError:
    print("⚠ El archivo no existe.")
except json.JSONDecodeError as e:
    print(f"⚠ JSON inválido: {e}")
except PermissionError:
    print("⚠ Sin permisos para leer el archivo.")
except Exception as e:
    print(f"⚠ Error inesperado: {e}")

# ESCRITURA DE ARCHIVO JSON:
try:
    with open("archivo.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)
    print("✓ Archivo creado correctamente.")
    
except TypeError as e:
    print(f"⚠ Tipo de dato no serializable: {e}")
except OSError as e:
    print(f"⚠ Error de E/S: {e}")
except Exception as e:
    print(f"⚠ Error inesperado: {e}")

# CONVERSIÓN DE CADENAS JSON:
try:
    datos = json.loads(cadena_json)
    print("✓ JSON parseado correctamente.")
    
except json.JSONDecodeError as e:
    print(f"⚠ JSON inválido en línea {e.lineno}, columna {e.colno}: {e.msg}")
except Exception as e:
    print(f"⚠ Error: {e}")
""")

# Ejemplo práctico de errores
print("\n--- EJEMPLOS de errores comunes ---\n")

# Error 1: JSON inválido
print("1. JSON inválido (falta comilla):")
try:
    json.loads('{"nombre: "Ana"}')
except json.JSONDecodeError as e:
    print(f"   ✗ JSONDecodeError: {e.msg}")

# Error 2: Archivo no existe
print("\n2. Archivo no existe:")
try:
    with open("archivo_inexistente.json", "r") as f:
        json.load(f)
except FileNotFoundError:
    print("   ✗ FileNotFoundError: El archivo no existe.")

# Error 3: Tipo no serializable
print("\n3. Tipo de dato no serializable:")
try:
    import datetime
    datos = {"fecha": datetime.datetime.now()}
    json.dumps(datos)
except TypeError as e:
    print(f"   ✗ TypeError: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 8. JSON ANIDADO (NESTED)
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("8. JSON ANIDADO (NESTED)")
print("=" * 80)

# EJEMPLO 1: Estructura compleja
print("\n--- EJEMPLO 1: Estructura compleja ---")

empresa = {
    "nombre": "TechCorp",
    "fundacion": 2010,
    "empleados": [
        {
            "id": 1,
            "nombre": "Ana García",
            "puesto": "CEO",
            "departamento": {
                "nombre": "Dirección",
                "ubicacion": "Madrid"
            },
            "proyectos": ["Proyecto A", "Proyecto B"]
        },
        {
            "id": 2,
            "nombre": "Luis Pérez",
            "puesto": "Developer",
            "departamento": {
                "nombre": "IT",
                "ubicacion": "Barcelona"
            },
            "proyectos": ["Proyecto C"]
        }
    ],
    "oficinas": {
        "principal": {
            "ciudad": "Madrid",
            "direccion": "Calle Mayor 1"
        },
        "secundaria": {
            "ciudad": "Barcelona",
            "direccion": "Paseo de Gracia 100"
        }
    }
}

# Guardar
with open("empresa.json", "w", encoding="utf-8") as f:
    json.dump(empresa, f, ensure_ascii=False, indent=2)

# Leer y acceder a datos anidados
with open("empresa.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print(f"Empresa: {datos['nombre']}")
print(f"Primer empleado: {datos['empleados'][0]['nombre']}")
print(f"Departamento: {datos['empleados'][0]['departamento']['nombre']}")
print(f"Primer proyecto: {datos['empleados'][0]['proyectos'][0]}")
print(f"Oficina principal: {datos['oficinas']['principal']['ciudad']}")

# EJEMPLO 2: Recorrer estructura anidada
print("\n--- EJEMPLO 2: Recorrer JSON anidado ---")

for empleado in datos['empleados']:
    print(f"\n{empleado['nombre']} - {empleado['puesto']}")
    print(f"  Departamento: {empleado['departamento']['nombre']}")
    print(f"  Proyectos: {', '.join(empleado['proyectos'])}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 9. EJERCICIOS PRÁCTICOS COMPLETOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("9. EJERCICIOS PRÁCTICOS")
print("=" * 80)

# EJERCICIO 1: Filtrar datos y guardar en nuevo JSON
print("\n--- EJERCICIO 1: Filtrar países por continente ---")

def filtrar_paises_por_continente():
    """Lee paises.json, filtra por continente y guarda resultado"""
    try:
        with open("paises.json", "r", encoding="utf-8") as f:
            paises = json.load(f)
        
        # Filtrar por Europa (puedes cambiar el continente)
        continente_buscar = "Europa"
        filtrados = [p for p in paises if p["continente"] == continente_buscar]
        
        if filtrados:
            print(f"✓ Países en {continente_buscar}:")
            for p in filtrados:
                print(f"  - {p['nombre']} ({p['poblacion']} millones)")
            
            # Guardar resultado
            with open("paises_filtrados.json", "w", encoding="utf-8") as f:
                json.dump(filtrados, f, ensure_ascii=False, indent=2)
            
            print(f"\n✓ Archivo 'paises_filtrados.json' creado con {len(filtrados)} países.")
        else:
            print(f"⚠ No se encontraron países en {continente_buscar}.")
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"⚠ Error con el archivo JSON: {e}")
    except Exception as e:
        print(f"⚠ Error inesperado: {e}")

filtrar_paises_por_continente()

# EJERCICIO 2: Agregar datos a JSON existente
print("\n--- EJERCICIO 2: Agregar nuevo país a JSON ---")

def agregar_pais(nombre, continente, poblacion):
    """Agrega un nuevo país al archivo paises.json"""
    try:
        # Leer datos existentes
        with open("paises.json", "r", encoding="utf-8") as f:
            paises = json.load(f)
        
        # Agregar nuevo país
        nuevo_pais = {
            "nombre": nombre,
            "continente": continente,
            "poblacion": poblacion
        }
        paises.append(nuevo_pais)
        
        # Guardar actualizado
        with open("paises.json", "w", encoding="utf-8") as f:
            json.dump(paises, f, ensure_ascii=False, indent=2)
        
        print(f"✓ País '{nombre}' agregado correctamente.")
        print(f"  Total de países ahora: {len(paises)}")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

agregar_pais("Argentina", "América", 45)

# EJERCICIO 3: Convertir CSV a JSON
print("\n--- EJERCICIO 3: Convertir lista Python a JSON ---")

def crear_catalogo_json():
    """Crea un catálogo de productos en formato JSON"""
    catalogo = {
        "tienda": "MiTienda Online",
        "actualizado": "2024-01-15",
        "productos": [
            {
                "id": "P001",
                "nombre": "Laptop HP",
                "categoria": "Electrónica",
                "precio": 899.99,
                "stock": 15,
                "disponible": True
            },
            {
                "id": "P002",
                "nombre": "Mouse Logitech",
                "categoria": "Accesorios",
                "precio": 25.50,
                "stock": 50,
                "disponible": True
            },
            {
                "id": "P003",
                "nombre": "Teclado Mecánico",
                "categoria": "Accesorios",
                "precio": 120.00,
                "stock": 0,
                "disponible": False
            }
        ]
    }
    
    try:
        with open("catalogo.json", "w", encoding="utf-8") as f:
            json.dump(catalogo, f, ensure_ascii=False, indent=2)
        
        print("✓ Catálogo JSON creado con éxito.")
        print(f"  Tienda: {catalogo['tienda']}")
        print(f"  Productos: {len(catalogo['productos'])}")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

crear_catalogo_json()

# EJERCICIO 4: Actualizar valores en JSON
print("\n--- EJERCICIO 4: Actualizar stock de producto ---")

def actualizar_stock_producto(producto_id, nuevo_stock):
    """Actualiza el stock de un producto en el catálogo"""
    try:
        with open("catalogo.json", "r", encoding="utf-8") as f:
            catalogo = json.load(f)
        
        # Buscar y actualizar producto
        encontrado = False
        for producto in catalogo['productos']:
            if producto['id'] == producto_id:
                producto['stock'] = nuevo_stock
                producto['disponible'] = nuevo_stock > 0
                encontrado = True
                print(f"✓ Stock de '{producto['nombre']}' actualizado a {nuevo_stock}")
                break
        
        if not encontrado:
            print(f"⚠ Producto con ID '{producto_id}' no encontrado.")
            return
        
        # Guardar cambios
        with open("catalogo.json", "w", encoding="utf-8") as f:
            json.dump(catalogo, f, ensure_ascii=False, indent=2)
        
        print("✓ Catálogo actualizado.")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

actualizar_stock_producto("P003", 25)

# EJERCICIO 5: Combinar múltiples JSON
print("\n--- EJERCICIO 5: Combinar múltiples archivos JSON ---")

def combinar_json_files():
    """Combina datos de múltiples archivos JSON"""
    # Crear archivos de ejemplo
    usuarios1 = [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}]
    usuarios2 = [{"id": 3, "nombre": "María"}, {"id": 4, "nombre": "Carlos"}]
    
    with open("usuarios1.json", "w", encoding="utf-8") as f:
        json.dump(usuarios1, f)
    with open("usuarios2.json", "w", encoding="utf-8") as f:
        json.dump(usuarios2, f)
    
    try:
        # Leer ambos archivos
        with open("usuarios1.json", "r") as f:
            datos1 = json.load(f)
        with open("usuarios2.json", "r") as f:
            datos2 = json.load(f)
        
        # Combinar
        todos_usuarios = datos1 + datos2
        
        # Guardar combinado
        with open("todos_usuarios.json", "w", encoding="utf-8") as f:
            json.dump(todos_usuarios, f, indent=2)
        
        print(f"✓ Archivos combinados: {len(todos_usuarios)} usuarios total.")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

combinar_json_files()

print("\n" + "=" * 80)
print("FIN DE LA GUÍA DE FICHEROS JSON")
print("=" * 80)
print("Usa Ctrl+F para buscar rápidamente cualquier operación que necesites.")
print()
print("RECORDATORIOS CLAVE:")
print("  • json.load()  → Leer desde archivo")
print("  • json.dump()  → Escribir a archivo")
print("  • json.loads() → Convertir cadena a Python")
print("  • json.dumps() → Convertir Python a cadena")
print("  • Siempre usar: ensure_ascii=False para caracteres especiales")
print("  • Siempre usar: indent=2 o indent=4 para formato legible")
print("=" * 80)
