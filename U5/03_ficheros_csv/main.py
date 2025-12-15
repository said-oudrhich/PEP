"""
═══════════════════════════════════════════════════════════════════════════
GUÍA COMPLETA: FICHEROS CSV EN PYTHON
═══════════════════════════════════════════════════════════════════════════

Este archivo contiene TODOS los ejemplos y operaciones con archivos CSV que 
necesitas para el examen. Usa Ctrl+F para buscar rápidamente lo que necesites.

ÍNDICE RÁPIDO (busca estos títulos):
1. LECTURA BÁSICA CON csv.reader
2. LECTURA CON csv.DictReader
3. ESCRITURA BÁSICA CON csv.writer
4. ESCRITURA CON csv.DictWriter
5. DELIMITADORES PERSONALIZADOS
6. MANEJO DE ERRORES
7. PROCESAMIENTO DE DATOS (filtrado, estadísticas, ordenación)
8. EJERCICIOS PRÁCTICOS COMPLETOS

═══════════════════════════════════════════════════════════════════════════
"""

import csv
from csv import reader, writer, DictReader, DictWriter

# ═══════════════════════════════════════════════════════════════════════════
# 1. LECTURA BÁSICA CON csv.reader
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("1. LECTURA BÁSICA CON csv.reader")
print("=" * 80)

# EJEMPLO 1: Lectura simple línea por línea
print("\n--- EJEMPLO 1: Lectura simple de CSV ---")
try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector_csv = reader(archivo)
        
        # Leer y mostrar cabecera
        cabecera = next(lector_csv, None)
        print(f"Cabecera: {cabecera}")
        
        # Leer datos fila por fila
        print("\nDatos:")
        for fila in lector_csv:
            print(f"  La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes.")

except FileNotFoundError:
    print("⚠ Error: El archivo 'ciudades.csv' no existe.")
except PermissionError:
    print("⚠ Error: No tienes permiso para leer el archivo.")
except Exception as e:
    print(f"⚠ Error inesperado: {e}")

# EJEMPLO 2: Leer todo el CSV en una lista
print("\n--- EJEMPLO 2: Leer todo el CSV en una lista ---")
try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector_csv = reader(archivo)
        datos = list(lector_csv)
        
        print(f"Total de filas (incluyendo cabecera): {len(datos)}")
        print(f"Cabecera: {datos[0]}")
        print(f"Primera ciudad: {datos[1]}")
        print(f"Última ciudad: {datos[-1]}")
        
        # Acceder a columnas específicas
        print("\nTodas las ciudades:")
        for i in range(1, len(datos)):
            print(f"  - {datos[i][0]}")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

# EJEMPLO 3: Saltar filas
print("\n--- EJEMPLO 3: Saltar la cabecera ---")
try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector_csv = reader(archivo)
        next(lector_csv, None)  # Saltar primera línea (cabecera)
        
        for fila in lector_csv:
            print(f"  {fila[0]}: {fila[2]}M habitantes")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 2. LECTURA CON csv.DictReader
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("2. LECTURA CON csv.DictReader")
print("=" * 80)

# EJEMPLO 1: DictReader con cabecera en el archivo
print("\n--- EJEMPLO 1: DictReader automático ---")
try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector = DictReader(archivo)
        
        print(f"Nombres de columnas: {lector.fieldnames}")
        
        for fila in lector:
            # Acceso por nombre de columna
            print(f"  {fila['Ciudad']} ({fila['País']}) - {fila['Población (millones)']}M hab.")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

# EJEMPLO 2: DictReader SIN cabecera (definir fieldnames manualmente)
print("\n--- EJEMPLO 2: DictReader con fieldnames manuales ---")
try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        campos = ["Ciudad", "País", "Población (millones)"]
        
        # Detectar si tiene cabecera
        primera_linea = archivo.readline().strip()
        archivo.seek(0)  # Reiniciar posición del archivo
        
        if primera_linea.split(",") == campos:
            # Tiene cabecera
            lector = DictReader(archivo)
            print("✓ Archivo CON cabecera detectada")
        else:
            # No tiene cabecera
            lector = DictReader(archivo, fieldnames=campos)
            print("✓ Archivo SIN cabecera, usando campos manuales")
        
        print(f"Campos: {lector.fieldnames}")
        
        for fila in lector:
            print(f"  {fila['Ciudad']} en {fila['País']}")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

# EJEMPLO 3: DictReader con delimitador personalizado
print("\n--- EJEMPLO 3: DictReader con delimitador personalizado ---")
ejemplo_delim = """Nombre;Edad;Ciudad
Ana;25;Madrid
Luis;30;Barcelona
María;28;Valencia"""

with open("temp_delim.csv", "w", encoding="utf-8") as f:
    f.write(ejemplo_delim)

try:
    with open("temp_delim.csv", "r", encoding="utf-8") as archivo:
        lector = DictReader(archivo, delimiter=";")
        
        for fila in lector:
            print(f"  {fila['Nombre']} tiene {fila['Edad']} años y vive en {fila['Ciudad']}")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 3. ESCRITURA BÁSICA CON csv.writer
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("3. ESCRITURA BÁSICA CON csv.writer")
print("=" * 80)

# EJEMPLO 1: Escribir datos básicos
print("\n--- EJEMPLO 1: Escribir CSV básico ---")

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
        
        # Opción 1: Escribir cabecera primero
        escritor_csv.writerow(capitales[0])
        
        # Opción 2: Escribir todas las filas de datos
        escritor_csv.writerows(capitales[1:])
        
    print("✓ Archivo 'capitales.csv' creado correctamente.")
    
except OSError as e:
    print(f"⚠ Error de E/S: {e.strerror}")

# EJEMPLO 2: Escribir fila por fila
print("\n--- EJEMPLO 2: Escribir fila por fila ---")

try:
    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo)
        
        # Escribir cabecera
        escritor.writerow(["Producto", "Precio", "Stock"])
        
        # Escribir filas individuales
        escritor.writerow(["Teclado", 29.99, 15])
        escritor.writerow(["Ratón", 12.50, 30])
        escritor.writerow(["Monitor", 199.00, 8])
        
    print("✓ Archivo 'productos.csv' creado.")
    
except OSError as e:
    print(f"⚠ Error: {e}")

# EJEMPLO 3: Modo append (añadir al final)
print("\n--- EJEMPLO 3: Añadir datos a un CSV existente ---")

try:
    # Añadir nueva fila al archivo existente
    with open("productos.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo)
        escritor.writerow(["Webcam", 45.00, 12])
        
    print("✓ Nueva fila añadida a 'productos.csv'.")
    
except OSError as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 4. ESCRITURA CON csv.DictWriter
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("4. ESCRITURA CON csv.DictWriter")
print("=" * 80)

# EJEMPLO 1: DictWriter básico
print("\n--- EJEMPLO 1: DictWriter básico ---")

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"},
]

try:
    with open("patrimonios.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        fieldnames = ["Ciudad", "País", "Lugar emblemático"]
        escritor_csv = DictWriter(archivo_csv, fieldnames=fieldnames)
        
        # Escribir cabecera
        escritor_csv.writeheader()
        
        # Escribir todas las filas
        escritor_csv.writerows(patrimonios)
        
    print("✓ Archivo 'patrimonios.csv' generado correctamente.")
    
except OSError as e:
    print(f"⚠ Error de E/S: {e.strerror}")

# EJEMPLO 2: DictWriter con delimitador personalizado
print("\n--- EJEMPLO 2: DictWriter con delimitador ';' ---")

empleados = [
    {"Nombre": "Ana García", "Departamento": "IT", "Salario": 45000},
    {"Nombre": "Luis Pérez", "Departamento": "RRHH", "Salario": 38000},
    {"Nombre": "María López", "Departamento": "Ventas", "Salario": 42000},
]

try:
    with open("empleados.csv", "w", newline="", encoding="utf-8") as archivo:
        fieldnames = ["Nombre", "Departamento", "Salario"]
        escritor = DictWriter(archivo, fieldnames=fieldnames, delimiter=";")
        
        escritor.writeheader()
        escritor.writerows(empleados)
        
    print("✓ Archivo 'empleados.csv' creado con delimitador ';'.")
    
except OSError as e:
    print(f"⚠ Error: {e}")

# EJEMPLO 3: DictWriter escribiendo fila por fila
print("\n--- EJEMPLO 3: DictWriter fila por fila ---")

try:
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        fieldnames = ["ID", "Artículo", "Cantidad"]
        escritor = DictWriter(archivo, fieldnames=fieldnames)
        
        escritor.writeheader()
        
        # Escribir filas individuales
        escritor.writerow({"ID": 1, "Artículo": "Silla", "Cantidad": 50})
        escritor.writerow({"ID": 2, "Artículo": "Mesa", "Cantidad": 20})
        escritor.writerow({"ID": 3, "Artículo": "Lámpara", "Cantidad": 35})
        
    print("✓ Archivo 'inventario.csv' creado.")
    
except OSError as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 5. DELIMITADORES PERSONALIZADOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("5. DELIMITADORES PERSONALIZADOS")
print("=" * 80)

print("\n--- EJEMPLO: Delimitadores comunes ---")

# Delimitador tabulador (TSV)
print("\n1. Tabulador (TSV):")
try:
    with open("datos_tab.tsv", "w", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo, delimiter="\t")
        escritor.writerow(["Nombre", "Edad", "Ciudad"])
        escritor.writerow(["Carlos", "25", "Madrid"])
        escritor.writerow(["Laura", "30", "Barcelona"])
    print("✓ Archivo TSV creado.")
except OSError as e:
    print(f"⚠ Error: {e}")

# Delimitador punto y coma
print("\n2. Punto y coma (;):")
try:
    with open("datos_semicolon.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo, delimiter=";")
        escritor.writerow(["Producto", "Precio"])
        escritor.writerow(["Laptop", "899.99"])
        escritor.writerow(["Tablet", "299.99"])
    print("✓ Archivo con ';' creado.")
except OSError as e:
    print(f"⚠ Error: {e}")

# Delimitador pipe
print("\n3. Pipe (|):")
try:
    with open("datos_pipe.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo, delimiter="|")
        escritor.writerow(["ID", "Descripción"])
        escritor.writerow(["001", "Primer registro"])
        escritor.writerow(["002", "Segundo registro"])
    print("✓ Archivo con '|' creado.")
except OSError as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 6. MANEJO DE ERRORES
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("6. MANEJO DE ERRORES")
print("=" * 80)

print("\n--- PLANTILLA COMPLETA de manejo de errores ---\n")

print("""
# LECTURA con manejo completo de errores:
try:
    with open("archivo.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
            
except FileNotFoundError:
    print("⚠ El archivo no existe.")
except PermissionError:
    print("⚠ No tienes permisos para leer el archivo.")
except UnicodeDecodeError:
    print("⚠ Error de codificación. Prueba con encoding='latin-1'.")
except Exception as e:
    print(f"⚠ Error inesperado: {e}")
    
# ESCRITURA con manejo completo de errores:
try:
    with open("archivo.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["dato1", "dato2"])
        
except OSError as e:
    print(f"⚠ Error de E/S: {e.strerror}")
except PermissionError:
    print("⚠ No tienes permisos para escribir.")
except Exception as e:
    print(f"⚠ Error inesperado: {e}")
else:
    print("✓ Archivo creado correctamente.")
""")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 7. PROCESAMIENTO DE DATOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("7. PROCESAMIENTO DE DATOS")
print("=" * 80)

# EJEMPLO 1: Calcular estadísticas (media de notas)
print("\n--- EJEMPLO 1: Calcular media de notas ---")

# Crear archivo de notas de ejemplo
notas_data = """Alumno,Matemáticas,Física,Química
Ana,8.5,7.0,9.0
Luis,6.0,7.5,6.5
María,9.0,8.5,9.5
Carlos,7.0,6.0,7.5"""

with open("notas.csv", "w", encoding="utf-8") as f:
    f.write(notas_data)

try:
    with open("notas.csv", "r", encoding="utf-8") as archivo:
        lector = DictReader(archivo)
        
        print(f"{'Alumno':<10} | {'Mate':<6} | {'Física':<6} | {'Química':<6} | {'Media':<6}")
        print("-" * 52)
        
        for fila in lector:
            alumno = fila['Alumno']
            mate = float(fila['Matemáticas'])
            fisica = float(fila['Física'])
            quimica = float(fila['Química'])
            media = round((mate + fisica + quimica) / 3, 2)
            
            print(f"{alumno:<10} | {mate:<6} | {fisica:<6} | {quimica:<6} | {media:<6}")

except FileNotFoundError:
    print("⚠ El archivo no existe.")

# EJEMPLO 2: Filtrar datos
print("\n--- EJEMPLO 2: Filtrar alumnos con media >= 7.5 ---")

try:
    aprobados = []
    
    with open("notas.csv", "r", encoding="utf-8") as archivo:
        lector = DictReader(archivo)
        
        for fila in lector:
            mate = float(fila['Matemáticas'])
            fisica = float(fila['Física'])
            quimica = float(fila['Química'])
            media = round((mate + fisica + quimica) / 3, 2)
            
            if media >= 7.5:
                aprobados.append({
                    'Alumno': fila['Alumno'],
                    'Media': media
                })
    
    # Guardar aprobados en nuevo CSV
    with open("aprobados.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = DictWriter(archivo, fieldnames=['Alumno', 'Media'])
        escritor.writeheader()
        escritor.writerows(aprobados)
    
    print(f"✓ {len(aprobados)} alumnos con media >= 7.5 guardados en 'aprobados.csv'")
    
except Exception as e:
    print(f"⚠ Error: {e}")

# EJEMPLO 3: Ordenar datos
print("\n--- EJEMPLO 3: Ordenar por nombre ---")

try:
    with open("notas.csv", "r", encoding="utf-8") as archivo:
        lector = DictReader(archivo)
        alumnos = list(lector)
    
    # Ordenar alfabéticamente
    alumnos_ordenados = sorted(alumnos, key=lambda x: x['Alumno'])
    
    # Guardar ordenado
    with open("notas_ordenadas.csv", "w", newline="", encoding="utf-8") as archivo:
        fieldnames = ['Alumno', 'Matemáticas', 'Física', 'Química']
        escritor = DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(alumnos_ordenados)
    
    print("✓ Alumnos ordenados guardados en 'notas_ordenadas.csv'")
    
except Exception as e:
    print(f"⚠ Error: {e}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 8. EJERCICIOS PRÁCTICOS COMPLETOS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("8. EJERCICIOS PRÁCTICOS")
print("=" * 80)

# EJERCICIO 1: Leer CSV, procesar y crear nuevo CSV
print("\n--- EJERCICIO 1: Agregar columna calculada ---")

def agregar_media_notas():
    """Lee notas.csv, calcula media y guarda en notas_con_media.csv"""
    try:
        with open("notas.csv", "r", encoding="utf-8") as archivo:
            lector = DictReader(archivo)
            datos = list(lector)
        
        # Agregar columna Media
        for fila in datos:
            mate = float(fila['Matemáticas'])
            fisica = float(fila['Física'])
            quimica = float(fila['Química'])
            fila['Media'] = round((mate + fisica + quimica) / 3, 2)
        
        # Escribir nuevo CSV
        with open("notas_con_media.csv", "w", newline="", encoding="utf-8") as archivo:
            fieldnames = ['Alumno', 'Matemáticas', 'Física', 'Química', 'Media']
            escritor = DictWriter(archivo, fieldnames=fieldnames)
            escritor.writeheader()
            escritor.writerows(datos)
        
        print("✓ Archivo 'notas_con_media.csv' creado con columna Media.")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

agregar_media_notas()

# EJERCICIO 2: Convertir lista de diccionarios a CSV
print("\n--- EJERCICIO 2: Exportar datos a CSV ---")

def exportar_catalogo_productos():
    """Crea un catálogo de productos en CSV"""
    productos = [
        {"codigo": "P001", "nombre": "Laptop Dell", "precio": 899.99, "stock": 15},
        {"codigo": "P002", "nombre": "Mouse Logitech", "precio": 25.50, "stock": 50},
        {"codigo": "P003", "nombre": "Teclado Mecánico", "precio": 120.00, "stock": 30},
        {"codigo": "P004", "nombre": "Monitor LG", "precio": 299.99, "stock": 10},
    ]
    
    try:
        with open("catalogo.csv", "w", newline="", encoding="utf-8") as archivo:
            fieldnames = ["codigo", "nombre", "precio", "stock"]
            escritor = DictWriter(archivo, fieldnames=fieldnames)
            escritor.writeheader()
            escritor.writerows(productos)
        
        print("✓ Catálogo de productos exportado a 'catalogo.csv'.")
        
    except OSError as e:
        print(f"⚠ Error: {e}")

exportar_catalogo_productos()

# EJERCICIO 3: Combinar dos CSVs
print("\n--- EJERCICIO 3: Combinar dos archivos CSV ---")

def combinar_csvs():
    """Combina dos CSVs con la misma estructura"""
    # Crear dos CSVs de ejemplo
    datos1 = [["Nombre", "Edad"], ["Ana", "25"], ["Luis", "30"]]
    datos2 = [["Nombre", "Edad"], ["María", "28"], ["Carlos", "35"]]
    
    with open("grupo1.csv", "w", newline="", encoding="utf-8") as f:
        writer(f).writerows(datos1)
    
    with open("grupo2.csv", "w", newline="", encoding="utf-8") as f:
        writer(f).writerows(datos2)
    
    # Combinar
    try:
        combinado = []
        
        # Leer primer archivo
        with open("grupo1.csv", "r", encoding="utf-8") as f:
            lector = reader(f)
            cabecera = next(lector)
            combinado.extend(list(lector))
        
        # Leer segundo archivo (sin cabecera)
        with open("grupo2.csv", "r", encoding="utf-8") as f:
            lector = reader(f)
            next(lector)  # Saltar cabecera
            combinado.extend(list(lector))
        
        # Escribir combinado
        with open("todos_grupos.csv", "w", newline="", encoding="utf-8") as f:
            escritor = writer(f)
            escritor.writerow(cabecera)
            escritor.writerows(combinado)
        
        print(f"✓ Archivos combinados: {len(combinado)} registros en 'todos_grupos.csv'.")
        
    except Exception as e:
        print(f"⚠ Error: {e}")

combinar_csvs()

print("\n" + "=" * 80)
print("FIN DE LA GUÍA DE FICHEROS CSV")
print("=" * 80)
print("Usa Ctrl+F para buscar rápidamente cualquier operación que necesites.")
print("Recuerda: SIEMPRE usar 'with open()' y 'newline=\"\"' al escribir CSV.")
print("=" * 80)
