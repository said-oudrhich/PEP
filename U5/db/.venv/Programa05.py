import mysql.connector
from mysql.connector import Error


def transaccion_ciudades():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            database="ciudades",
            user="ciudades",
            password="ciudades",
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            conexion.start_transaction()

            insertar_query = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"
            cursor.execute(insertar_query, ("Madrid", "España", 6.8))

            eliminar_query = "DELETE FROM ciudades WHERE poblacion_millones < %s"
            cursor.execute(eliminar_query, (10,))

            conexion.commit()
            print("Transacción completada con éxito.")
    except Error as e:
        print(f"Error: {e}")
        conexion.rollback()
        print("Transacción revertida por error.")
    finally:
        conexion.close()


if __name__ == "__main__":
    transaccion_ciudades()
