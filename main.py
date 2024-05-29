import streamlit as st
import pandas as pd

from pages.personalitytest import show_questionnaire

# Simulación de base de datos de usuarios
USER_DATA = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

def main():
    # Título de la aplicación
    st.title("Sistema de Login en Streamlit")

    # Estado de la sesión de usuario
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ''

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

    # Navegación entre páginas
    if st.session_state.logged_in:
        st.subheader(f"Bienvenido {st.session_state.username}")
        if st.button("Cerrar Sesión"):
            logout()
    else:
        login()

if __name__ == "__main__":
    main()
