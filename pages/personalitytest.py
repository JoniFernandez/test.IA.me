import streamlit as st
import pandas as pd
import os

# Simulación de base de datos de usuarios
USER_DATA = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

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

# Inicializar el archivo CSV si no existe
DATA_FILE = "responses.csv"
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Usuario"] + list(questions.keys()))
    df.to_csv(DATA_FILE, index=False)

# Función para mostrar el cuestionario y recopilar las respuestas
def show_questionnaire(username):
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

            # Agregar el nombre del usuario al DataFrame
            df.insert(0, "Usuario", username)

            # Guardar las respuestas en el archivo CSV
            if os.path.exists(DATA_FILE):
                existing_df = pd.read_csv(DATA_FILE)
                updated_df = pd.concat([existing_df, df], ignore_index=True)
            else:
                updated_df = df

            updated_df.to_csv(DATA_FILE, index=False)

            # Mostrar la tabla de respuestas
            st.write("Respuestas del cuestionario:")
            st.dataframe(updated_df)

def main():
    # Inicializar variables de estado
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.page = 'Login'

    # Título de la aplicación
    st.title("Sistema de Login en Streamlit")

    # Función para el formulario de login
    def login():
        st.subheader("Iniciar Sesión")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar Sesión"):
            if username in USER_DATA and USER_DATA[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.page = "Cuestionario"
                st.success(f"Bienvenido {username}!")
            else:
                st.error("Usuario o contraseña incorrectos")

    # Función para el formulario de logout
    def logout():
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.page = "Login"
        st.success("Has cerrado sesión exitosamente")

    # Navegación en la barra lateral
    if st.session_state.logged_in:
        st.sidebar.title("Navegación")
        if st.sidebar.button("Cerrar Sesión"):
            logout()

        page = st.sidebar.selectbox("Selecciona una página", ["Cuestionario"])

        if page == "Cuestionario":
            show_questionnaire(st.session_state.username)
    else:
        login()

if __name__ == "__main__":
    main()
