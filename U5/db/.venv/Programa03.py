import mysql.connector
from mysql.connector import Error


def insertar_ciudades(datos):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            database="ciudades",
            user="ciudades",
            password="ciudades",
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"
            cursor.executemany(sql, datos)
            conexion.commit()
            print(f"{cursor.rowcount} filas insertadas correctamente.")
    except Error as e:
        conexion.rollback()
        print(f"Error: {e}")
    finally:
        conexion.close()


if __name__ == "__main__":
    datos = [
        ("Tokio", "Japón", 37.4),
        ("Delhi", "India", 30.3),
        ("Shanghái", "China", 27.1),
        ("São Paulo", "Brasil", 22.0),
        ("Ciudad de México", "México", 21.7),
    ]
    insertar_ciudades(datos)
