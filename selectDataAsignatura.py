import mysql.connector
import pandas as pd
from mysql.connector import Error


def export_asignatura_to_excel():
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
            cursor.execute("SELECT idAsignatura, nombre, creditos FROM asignatura")

            # Obtén los nombres de las columnas
            column_names = [desc[0] for desc in cursor.description]

            # Obtén los datos
            records = cursor.fetchall()

            # Convertir los registros en un DataFrame de pandas
            df = pd.DataFrame(records, columns=column_names)

            # Exportar el DataFrame a un archivo Excel
            df.to_excel("asignatura-1.xlsx", index=False, engine='openpyxl')
            print("Los datos se han exportado a 'asignatura-1.xlsx' con éxito.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


if __name__ == "__main__":
    export_asignatura_to_excel()
