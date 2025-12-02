import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    sql = "SELECT * FROM series"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    print("Listado de series:")
    for fila in resultados:
        print(fila)

except Error as e:
    print(f"Error con MySQL: {e}")

finally:
    cursor.close()
    conexion.close()
    print("Conexión cerrada")
