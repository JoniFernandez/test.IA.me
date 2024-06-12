import streamlit as st

st.image('testiamelogo.jpg')

page_bg_color = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #3d0072;
}
</style>
'''
# Aplicar el CSS
st.markdown(page_bg_color, unsafe_allow_html=True)


st.title('Bienvenidos a Test.IA.me 🧠')
st.write("Navegue a la ventana de registro para guardar sus datos")
