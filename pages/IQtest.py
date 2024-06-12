import streamlit as st
from PIL import Image
import io
import psycopg2
import pandas as pd
import os


# Función para obtener conexión a la base de datos
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


# Definimos los colores de fondo
page_bg_color = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFBF0;
}
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)

# Definimos las preguntas y opciones
questions = {i: f'PREGUNTA{i}.png' for i in range(1, 41)}
options = {i: f'RESPUESTA{i}.png' for i in range(1, 41)}


# Función para autenticar al usuario
def authenticate_user():
    st.title("Cuestionario de IQ")
    user_id = st.text_input("Ingrese su ID de usuario")
    password = st.text_input("Ingrese su contraseña", type="password")
    if st.button("Iniciar sesión"):
        conn = get_db_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT password FROM public.user_profiles WHERE user_id = %s", (user_id,))
                result = cursor.fetchone()
                if result is None:
                    st.error("Usuario no registrado.")
                    return None
                elif result[0] != password:
                    st.error("Contraseña incorrecta.")
                    return None
                else:
                    st.success("Autenticación exitosa.")
                    st.session_state.authenticated = True
                    st.session_state.user_id = user_id
                    return user_id
            except psycopg2.Error as e:
                st.error("Error al verificar los datos del usuario: " + str(e))
            finally:
                cursor.close()
                conn.close()
    return None


# Función para obtener las respuestas correctas
def get_correct_answers():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM public.iq_results WHERE user_id = 'RESPUESTAS CORRECTAS'")
            correct_answers = cursor.fetchone()
            cursor.close()
            conn.close()
            return correct_answers[1:]  # Omitir el user_id en la comparación
        except psycopg2.Error as e:
            st.error("Error al obtener las respuestas correctas: " + str(e))
    return None


# Función para almacenar las respuestas y calcular el puntaje
def store_responses(user_id, responses):
    st.write("Respuestas del cuestionario:")
    if "" in responses.values():
        st.warning("Por favor completa todas las preguntas antes de enviar el cuestionario.")
    else:
        st.success("Cuestionario enviado exitosamente")
        df = pd.DataFrame([responses])

        conn = get_db_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                columns = ', '.join(['user_id'] + [f'question_{i}' for i in range(1, 41)])
                values = ', '.join(['%s'] * 41)
                sql = f'INSERT INTO "public"."iq_results" ({columns}) VALUES ({values})'
                cursor.execute(sql, [user_id] + df.iloc[0].tolist())
                conn.commit()
                st.success("Respuestas almacenadas exitosamente en la base de datos.")
                calculate_score_and_iq(user_id, responses)
                st.experimental_rerun()
            except psycopg2.Error as e:
                st.error("Error al insertar los datos en la base de datos: " + str(e))
            finally:
                cursor.close()
                conn.close()

        st.write("Respuestas del cuestionario:")
        st.dataframe(df)


# Función para calcular el puntaje y el IQ del usuario
def calculate_score_and_iq(user_id, user_responses):
    correct_answers = get_correct_answers()
    if correct_answers is not None:
        score = 0
        for i, (key, response) in enumerate(user_responses.items(), start=1):
            if response == correct_answers[i - 1]:
                score += 1

        # Calcular el IQ basado en el puntaje usando una escala predefinida
        if score <= 10:
            iq = 70 + score * 3
        elif score <= 20:
            iq = 100 + (score - 10) * 2
        elif score <= 30:
            iq = 120 + (score - 20) * 1.5
        else:
            iq = 135 + (score - 30) * 1

        st.success(f"El puntaje obtenido por {user_id} es: {score}/40")
        st.success(f"El IQ calculado es: {iq:.2f}")



# Función para mostrar el cuestionario
def show_questionnaire(user_id):
    if user_id:
        st.write("Por favor responda las siguientes preguntas:")
        responses = {}
        for key in range(1, 41):
            question_image_path = questions.get(key)
            if question_image_path:
                with open(question_image_path, 'rb') as f:
                    question_image_bytes = f.read()
                st.image(Image.open(io.BytesIO(question_image_bytes)), caption=f"Pregunta {key}")
            options_image_path = options.get(key)
            if options_image_path:
                with open(options_image_path, 'rb') as f:
                    options_image_bytes = f.read()
                st.image(Image.open(io.BytesIO(options_image_bytes)), caption=f"Opciones {key}")
            selected_option = st.radio(f"Selecciona una opción para la pregunta {key}:", ["a", "b", "c", "d", "e", "f"],
                                       key=key)
            responses[key] = selected_option

        if st.button("Enviar"):
            store_responses(user_id, responses)


# Inicialización de estado
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None

# Autenticación y cuestionario
if st.session_state.authenticated:
    show_questionnaire(st.session_state.user_id)
else:
    authenticate_user()
