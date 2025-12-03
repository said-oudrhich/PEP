import mysql.connector
from mysql.connector import Error


def consultar_ciudades():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            database="ciudades",
            user="ciudades",
            password="ciudades",
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            consulta = "SELECT nombre, poblacion_millones FROM ciudades WHERE poblacion_millones > %s"
            cursor.execute(consulta, (25,))
            resultados = cursor.fetchall()
            for fila in resultados:
                nombre, poblacion = fila
                print(f"Ciudad: {nombre}, Población: {poblacion} millones")
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()


if __name__ == "__main__":
    consultar_ciudades()
