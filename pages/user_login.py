import streamlit as st
import psycopg2
import os

admin_verification_pw = 'soy/admin/muy/copado'

# Configuración de la conexión utilizando variables de entorno
def get_db_connection():
    try:
        user = os.getenv('DB_USER', 'postgres.esjjksenzsaamvlmcfqo')
        password = os.getenv('DB_PASSWORD', 'Supabase2024#')
        host = os.getenv('DB_HOST', 'aws-0-us-west-1.pooler.supabase.com')
        port = os.getenv('DB_PORT', '6543')
        dbname = os.getenv('DB_NAME', 'postgres')
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except psycopg2.Error as e:
        st.error("Error al conectar con la base de datos: " + str(e))
        return None


def user_id_exists(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM user_profiles WHERE user_id = %s"
            cur.execute(query, (user_id,))
            result = cur.fetchone()
            return result is not None
    finally:
        conn.close()


def insert_user(user_id, nombre, apellido, password, is_admin):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO user_profiles (user_id, Name, Last_Name, password, admin_state) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (user_id, nombre, apellido, password, is_admin))
            conn.commit()
    except psycopg2.Error as e:
        st.error(f"Se produjo un error al guardar el usuario: {e}")
    finally:
        conn.close()

# Interfaz de Streamlit
# Título y foto en la misma fila

#st.image('labo.jpg')

st.title('✅ Registrar usuario ')

nombre = st.text_input("Nombre", max_chars=50)
apellido = st.text_input("Apellido", max_chars=50)
password = st.text_input("Password", max_chars=20)
user_id = st.text_input("digital_user_id", max_chars=50)
user_admin_state = st.radio("¿Eres administrador?", ("Sí", "No"))

if st.button('Guardar'):
    admin_state = True if user_admin_state == "Sí" else False
    if not nombre or not apellido or not user_id or not password:
        st.error("Por favor, completa todos los campos.")
    elif user_id_exists(user_id):
        st.error("El user_id ya está registrado. Por favor, utiliza otro email.")
    else:
        insert_user(user_id, nombre, apellido, password, admin_state)
        st.success("Usuario registrado exitosamente.")