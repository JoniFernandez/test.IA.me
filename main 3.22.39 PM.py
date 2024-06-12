import streamlit as st

# Mostrar una imagen
st.image('testiamelogo.png')

# Definir el color de fondo de la página
page_bg_color = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #3d0072;
}
</style>
'''
# Aplicar el CSS
st.markdown(page_bg_color, unsafe_allow_html=True)

# Título y texto con color blanco
st.markdown("<h1 style='color: white;'>Bienvenidos a Test.IA.me 🧠</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: white;'>Navegue a la ventana de registro {user login} para guardar sus datos!</p>", unsafe_allow_html=True)
