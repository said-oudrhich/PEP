import platform
import os

print("=== Información del sistema ===")

# Mostrar el procesador
print("Procesador:", platform.processor())

# Mostrar el sistema operativo y su versión
print("Sistema operativo:", platform.system(), platform.release())

# Mostrar el nombre del host
print("Nombre del host:", platform.node())

# Mostrar el directorio actual
print("Directorio actual:", os.getcwd())
