import streamlit as st
import psycopg2
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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

def get_b5_profile(user_id):
    conn = get_db_connection()
    if conn is None:
        return None
    cursor = conn.cursor()
    query = """
    SELECT extraversion, agreeableness, conscientiousness, emotionalstability, openness
    FROM "public"."B5_Personality_Test"
    WHERE user_id = %s;
    """
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insights(user_id):
    conn = get_db_connection()
    if conn is None:
        return None
    cursor = conn.cursor()
    query = """
    SELECT extraversion, agreeableness, conscientiousness, emotionalstability, openness
    FROM "B5_Personality_Test"
    WHERE user_id = %s;
    """
    cursor.execute(query, (user_id,))
    user_scores = cursor.fetchone()

    if user_scores is None:
        st.error("No se encontraron datos para el usuario proporcionado.")
        cursor.close()
        conn.close()
        return

    query_all = """
    SELECT b.extraversion, b.agreeableness, b.conscientiousness, b.emotionalstability, b.openness
    FROM "B5_Personality_Test" AS b
    JOIN "user_profiles" AS u ON b.user_id = u.user_id
    WHERE u.admin_state = False;
    """
    cursor.execute(query_all)
    all_scores = np.array(cursor.fetchall())
    cursor.close()
    conn.close()

    traits = ['extraversion', 'agreeableness', 'conscientiousness', 'emotionalstability', 'openness']
    for i, trait in enumerate(traits):
        fig, ax = plt.subplots()
        ax.hist(all_scores[:, i], bins=20, alpha=0.5, label='Non-admins')
        ax.axvline(x=user_scores[i], color='r', linestyle='dashed', linewidth=2, label=f'User {trait}')
        ax.set_title(f'Distribution of {trait}')
        ax.legend()
        st.pyplot(fig)

def main():
    st.title("Página de Perfiles de Usuario")
    if 'admin_verified' not in st.session_state:
        st.session_state['admin_verified'] = False

    user_id = st.text_input("Ingrese su ID de usuario", key="user_id")
    password = st.text_input("Ingrese su contraseña", type="password", key="password")

    if st.button('Verificar Usuario'):
        conn = get_db_connection()
        if conn is None:
            return
        try:
            cursor = conn.cursor()
            query = """
            SELECT admin_state FROM User_Profiles WHERE user_id = %s AND password = %s;
            """
            cursor.execute(query, (user_id, password))
            result = cursor.fetchone()
            if result is None:
                st.error("Usuario no encontrado o contraseña incorrecta.")
            elif not result[0]:
                st.error("Usted no tiene permisos de administrador.")
            else:
                st.success("Admin verificado. Acceso concedido.")
                st.session_state['admin_verified'] = True
        finally:
            cursor.close()
            conn.close()

    if st.session_state['admin_verified']:
        user_name = st.text_input("Ingrese el nombre de usuario para buscar", key="user_search")
        if st.button('Obtener perfil de usuario'):
            profile = get_b5_profile(user_name)
            if profile:
                st.write(f"Perfil de {user_name}: {profile}")
                insights(user_name)

                # Crear y mostrar el gráfico de torta
                labels = ['Extraversión', 'Amabilidad', 'Responsabilidad', 'Estabilidad Emocional', 'Apertura']
                fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(profile, labels=labels, autopct='%1.1f%%', startangle=140)
                ax.set_title('Distribución de Personalidad B5')
                st.pyplot(fig)
            else:
                st.error("Usuario no encontrado.")

if __name__ == "__main__":
    main()
