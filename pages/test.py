import psycopg2
import os

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres.esjjksenzsaamvlmcfqo",
            password="Supabase2024#",
            host="aws-0-us-west-1.pooler.supabase.com",
            port="6543"
        )
        return conn
    except psycopg2.Error as e:
        print("Error al conectar con la base de datos:", e)
        return None
    

def test_db_connection():
    conn = get_db_connection()
    if conn is not None:
        print("Conexión establecida con la base de datos.")
        try:
            cursor = conn.cursor()
            
            # Consulta para obtener el nombre de la base de datos actual
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()
            print("Conectado a la base de datos:", db_name[0])

            # Consulta para obtener el esquema actual
            cursor.execute("SELECT current_schema();")
            current_schema = cursor.fetchone()
            print("Esquema actual:", current_schema[0])

            cursor.close()
        except psycopg2.Error as e:
            print("Error al realizar la consulta:", e)
        finally:
            conn.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")
   
if __name__ == "__main__":
    test_db_connection()
