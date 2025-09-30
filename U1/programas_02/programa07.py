minutos = int(input("Introduce una cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(
    str(minutos)
    + " minutos son "
    + str(horas)
    + " horas y "
    + str(minutos_restantes)
    + " minutos."
)
