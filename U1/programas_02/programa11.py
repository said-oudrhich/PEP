h = int(input("Introduce la hora de salida (0-23): "))
m = int(input("Introduce los minutos de salida (0-59): "))
s = int(input("Introduce los segundos de salida (0-59): "))
n = int(input("Introduce el tiempo de viaje en segundos: "))

total_segundos = h * 3600 + m * 60 + s + n
h_llegada = (total_segundos // 3600) % 24
m_llegada = (total_segundos % 3600) // 60
s_llegada = total_segundos % 60

print(
    "La hora de llegada a la ciudad B es:",
    str(h_llegada) + ":" + str(m_llegada) + ":" + str(s_llegada),
)
