import mysql.connector
from mysql.connector import Error
import random
import faker

# Inicializa el generador de datos ficticios
fake = faker.Faker()

def insert_random_record():
    try:
        # Conectarse a la base de datos MySQL
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto según tu configuración
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Generar datos aleatorios
            id_asignatura = random.randint(1, 1000)  # Ajusta el rango según tus necesidades
            nombre_asignatura = fake.word()
            descripcion_asignatura = fake.sentence()

            # Inserción de datos en la tabla
            insert_query = """
            INSERT INTO asignatura (curso, nombre, descripcion)
            VALUES (%s, %s, %s)
            """
            record = (id_asignatura, nombre_asignatura, descripcion_asignatura)

            cursor.execute(insert_query, record)
            connection.commit()

            print("Registro insertado con éxito.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    insert_random_record()
