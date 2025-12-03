import mysql.connector
from mysql.connector import Error


def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost", database="ciudades", user="ciudades", password="ciudades"
        )
        if conexion.is_connected():
            print("Conexión establecida correctamente")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        if "conexion" in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")


if __name__ == "__main__":
    conectar_base_datos()
