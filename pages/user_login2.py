import streamlit as st
import psycopg2
import os

admin_verification_pw = 'soy/admin/muy/copado'
page_bg_color = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #3d0072;
}

h1, h2, h3, h4, h5, h6, label, div.st-bq, div.stRadio > div > label {
    color: white !important;
}

input {
    color: black !important;
    background-color: white !important;
}
</style>
'''
# Aplicar el CSS
st.markdown(page_bg_color, unsafe_allow_html=True)

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
st.title('✅ Registrar usuario ')

nombre = st.text_input("Nombre", max_chars=50)
apellido = st.text_input("Apellido", max_chars=50)
password = st.text_input("Password", max_chars=20, type='password')
user_id = st.text_input("Digital User ID", max_chars=50)
user_admin_state = st.radio("¿Eres administrador?", ("Sí", "No"))

admin_verification_password = None
if user_admin_state == "Sí":
    admin_verification_password = st.text_input("Contraseña de verificación de administrador", type='password')

if st.button('Guardar'):
    admin_state = True if user_admin_state == "Sí" else False
    if not nombre or not apellido or not user_id or not password or (admin_state and not admin_verification_password):
        st.error("Por favor, completa todos los campos.")
    elif user_id_exists(user_id):
        st.error("El user_id ya está registrado. Por favor, utiliza otro nombre de usuario.")
    else:
        if admin_state:
            if admin_verification_password == admin_verification_pw:
                insert_user(user_id, nombre, apellido, password, admin_state)
                st.success("Usuario administrador registrado exitosamente.")
            else:
                st.error("Contraseña de verificación de administrador incorrecta.")
        else:
            insert_user(user_id, nombre, apellido, password, admin_state)
            st.success("Usuario registrado exitosamente.")
