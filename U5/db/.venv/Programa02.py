import mysql.connector
from mysql.connector import Error


def crear_tabla_ciudades():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            database="ciudades",
            user="ciudades",
            password="ciudades",
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            crear_tabla_query = """
            CREATE TABLE ciudades (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                pais VARCHAR(50),
                poblacion_millones FLOAT
            );
            """
            cursor.execute(crear_tabla_query)
            print("Tabla creada correctamente")
    except Error as e:
        if e.errno == 1050:  # Codigo de error para "tabla ya existe"
            print("Error: La tabla ya existe.")
        else:
            print(f"Error al crear la tabla: {e}")
    finally:
        if "conexion" in locals() and conexion.is_connected():
            conexion.close()


if __name__ == "__main__":
    crear_tabla_ciudades()
