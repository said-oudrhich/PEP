"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

anio = int(input("Introduce el año: "))
mes = int(input("Introduce el mes: "))
dia = int(input("Introduce el día: "))

fecha_correcta = False

if 1 <= mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            fecha_correcta = True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            fecha_correcta = True
    elif mes == 2:
        # Comprobar si es bisiesto
        es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        if es_bisiesto:
            if 1 <= dia <= 29:
                fecha_correcta = True
        else:
            if 1 <= dia <= 28:
                fecha_correcta = True

if fecha_correcta:
    print(f"La fecha {dia}/{mes}/{anio} es correcta.")
else:
    print(f"La fecha {dia}/{mes}/{anio} es incorrecta.")
