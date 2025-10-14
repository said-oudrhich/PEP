def a_binario(n):
    """Convierte un número entero a binario en forma de cadena"""
    if isinstance(n, int):
        return bin(n)[2:]
    return "Error: no es un entero válido"

def a_hexadecimal(n):
    """Convierte un número entero a hexadecimal en forma de cadena"""
    if isinstance(n, int):
        return hex(n)[2:].upper()
    return "Error: no es un entero válido"

def a_entero(texto):
    """Convierte una cadena numérica a entero, controlando errores"""
    if texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit()):
        return int(texto)
    return "Error: la cadena no es un número válido"
