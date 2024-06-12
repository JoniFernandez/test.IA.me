import streamlit as st
import psycopg2
import pandas as pd
import os
def getExtraversionScore(df):
    """To Calcualte the Extraversion Score"""
    ExtraversionScore = 0
    ExtraversionScore = 20 + df['EXT1'] - df['EXT2'] + df['EXT3'] - df['EXT4'] + df['EXT5'] - df['EXT6'] + df['EXT7'] - df['EXT8'] + df['EXT9'] - df['EXT10']
    return ExtraversionScore

def getAgreeablenessScore(df):
    """To Calcualte the Agreeableness Score"""
    AgreeablenessScore = 0
    AgreeablenessScore = 14 - df['AGR1'] + df['AGR2'] - df['AGR3'] + df['AGR4'] - df['AGR5'] + df['AGR6'] - df['AGR7'] + df['AGR8'] + df['AGR9'] + df['AGR10']
    return AgreeablenessScore

def getConscientiousnessScore(df):
    """To Calcualte the Conscientiousness Score"""
    ConscientiousnessScore = 0
    ConscientiousnessScore = 14 + df['CSN1'] - df['CSN2'] + df['CSN3'] - df['CSN4'] + df['CSN5'] - df['CSN6'] + df['CSN7'] - df['CSN8'] + df['CSN9'] + df['CSN10']
    return ConscientiousnessScore

def getEmotionalStabilityScore(df):
    """To Calcualte the EmotionalStability Score"""
    EmotionalStabilityScore = 0
    EmotionalStabilityScore = 38 - df['EST1'] + df['EST2'] - df['EST3'] + df['EST4'] - df['EST5'] - df['EST6'] - df['EST7'] - df['EST8'] - df['EST9'] - df['EST10']
    return EmotionalStabilityScore

def getOpennessScore(df):
    """To Calcualte the Openness Score"""
    OpennessScore = 0
    OpennessScore = 8 + df['OPN1'] - df['OPN2'] + df['OPN3'] - df['OPN4'] + df['OPN5'] - df['OPN6'] + df['OPN7'] + df['OPN8'] + df['OPN9'] + df['OPN10']
    return OpennessScore

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

# Preguntas del cuestionario
questions = {
    'EXT1': 'Soy el alma de la fiesta.',
    'EXT2': 'No hablo mucho.',
    'EXT3': 'Me siento cómodo alrededor de las personas.',
    'EXT4': 'Me mantengo en segundo plano.',
    'EXT5': 'Inicio conversaciones.',
    'EXT6': 'Tengo poco que decir.',
    'EXT7': 'Hablo con mucha gente diferente en las fiestas.',
    'EXT8': 'No me gusta llamar la atención sobre mí mismo.',
    'EXT9': 'No me importa ser el centro de atención.',
    'EXT10': 'Soy tranquilo con los desconocidos.',
    'AGR1': 'Me preocupo poco por los demás.',
    'AGR2': 'Estoy interesado en la gente.',
    'AGR3': 'Insulto a la gente.',
    'AGR4': 'Siento simpatía por los sentimientos de los demás.',
    'AGR5': 'No me interesan los problemas de otras personas.',
    'AGR6': 'Tengo un corazón blando.',
    'AGR7': 'Realmente no estoy interesado en los demás.',
    'AGR8': 'Tomo tiempo para los demás.',
    'AGR9': 'Siento las emociones de los demás.',
    'AGR10': 'Hago que la gente se sienta cómoda.',
    'EST1': 'Me estreso fácilmente.',
    'EST2': 'Estoy relajado la mayor parte del tiempo.',
    'EST3': 'Me preocupo por las cosas.',
    'EST4': 'Raramente me siento triste.',
    'EST5': 'Me molesto fácilmente.',
    'EST6': 'Me altero fácilmente.',
    'EST7': 'Cambio mucho de humor.',
    'EST8': 'Tengo cambios de humor frecuentes.',
    'EST9': 'Me irrito fácilmente.',
    'EST10': 'A menudo me siento triste.',
    'CSN1': 'Siempre estoy preparado.',
    'CSN2': 'Dejo mis pertenencias por ahí.',
    'CSN3': 'Presto atención a los detalles.',
    'CSN4': 'Estropeo las cosas.',
    'CSN5': 'Hago las tareas de inmediato.',
    'CSN6': 'A menudo olvido poner las cosas en su lugar adecuado.',
    'CSN7': 'Me gusta el orden.',
    'CSN8': 'Evito mis responsabilidades.',
    'CSN9': 'Sigo un horario.',
    'CSN10': 'Soy exigente en mi trabajo.',
    'OPN1': 'Tengo un vocabulario rico.',
    'OPN2': 'Tengo dificultad para entender ideas abstractas.',
    'OPN3': 'Tengo una imaginación vívida.',
    'OPN4': 'No estoy interesado en ideas abstractas.',
    'OPN5': 'Tengo excelentes ideas.',
    'OPN6': 'No tengo una buena imaginación.',
    'OPN7': 'Entiendo las cosas rápidamente.',
    'OPN8': 'Uso palabras difíciles.',
    'OPN9': 'Paso tiempo reflexionando sobre las cosas.',
    'OPN10': 'Estoy lleno de ideas.'
}


# Función para mostrar el cuestionario y recopilar las respuestas
def show_questionnaire(user_id):
    st.title("Cuestionario de Personalidad")

    st.write("Por favor responde las siguientes preguntas:")

    responses = {}  # Diccionario para almacenar las respuestas del usuario
    for key, value in questions.items():
        selected_option = st.radio(value, ["En desacuerdo", "Parcialmente en desacuerdo", "Neutral",
                                           "Parcialmente de acuerdo", "De acuerdo"], key=key)
        responses[key] = selected_option

    if st.button("Enviar"):
        if "" in responses.values():
            st.warning("Por favor completa todas las preguntas antes de enviar el cuestionario.")
        else:
            st.success("Cuestionario enviado exitosamente")
            # Procesar las respuestas y crear un DataFrame
            df = pd.DataFrame([responses])
            # Reemplazar las respuestas con sus equivalentes numéricos
            mapping = {
                "En desacuerdo": 1,
                "Parcialmente en desacuerdo": 2,
                "Neutral": 3,
                "Parcialmente de acuerdo": 4,
                "De acuerdo": 5
            }
            df = df.replace(mapping)

            # Calcular puntuaciones de los rasgos de personalidad
            df['extraversion'] = getExtraversionScore(df)
            df['agreeableness'] = getAgreeablenessScore(df)
            df['conscientiousness'] = getConscientiousnessScore(df)
            df['emotionalstability'] = getEmotionalStabilityScore(df)
            df['openness'] = getOpennessScore(df)

            # Guardar las respuestas en la base de datos
            conn = get_db_connection()
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    columns = ', '.join(df.columns)
                    values = ', '.join(['%s'] * len(df.columns))
                    sql = f'INSERT INTO "public"."B5_Personality_Test" (user_id, {columns}) VALUES (%s, {values})'
                    cursor.execute(sql, [user_id] + df.iloc[0].tolist())
                    conn.commit()
                except psycopg2.Error as e:
                    st.error("Error al insertar los datos en la base de datos: " + str(e))
                finally:
                    cursor.close()
                    conn.close()

            # Mostrar la tabla de respuestas
            st.write("Respuestas del cuestionario:")
            st.dataframe(df)

def authenticate_and_show_questionnaire():
    st.title("Autenticación")
    user_id = st.text_input("Ingrese su ID de usuario")
    password = st.text_input("Ingrese su contraseña", type="password")

    if st.button("Iniciar sesión"):
        conn = get_db_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                # Verificar si el usuario y la contraseña son correctos
                cursor.execute("SELECT password FROM public.user_profiles WHERE user_id = %s", (user_id,))
                result = cursor.fetchone()
                if result is None:
                    st.error("Usuario no registrado.")
                elif result[0] != password:
                    st.error("Contraseña incorrecta.")
                else:
                    st.success("Autenticación exitosa.")
            except psycopg2.Error as e:
                st.error("Error al verificar los datos del usuario: " + str(e))
            finally:
                cursor.close()
                conn.close()
                return user_id
        else:
            st.error("No se pudo establecer conexión con la base de datos.")
    return user_id


# Llamar a la función de autenticación en lugar de show_questionnaire directamente
show_questionnaire(authenticate_and_show_questionnaire())