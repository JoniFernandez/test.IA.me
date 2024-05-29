import streamlit as st
from PIL import Image
import io


page_bg_color = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFBF0;
}
</style>
'''

# Aplicar el CSS
st.markdown(page_bg_color, unsafe_allow_html=True)


questions = {
    1: 'PREGUNTA1.png',
    2: 'PREGUNTA2.png',
    3: 'PREGUNTA3.png',
    4: 'PREGUNTA4.png',
    5: 'PREGUNTA5.png',
    6: 'PREGUNTA6.png',
    7: 'PREGUNTA7.png',
    8: 'PREGUNTA8.png',
    9: 'PREGUNTA9.png',
    10: 'PREGUNTA10.png',
    11: 'PREGUNTA11.png',
    12: 'PREGUNTA12.png',
    13: 'PREGUNTA13.png',
    14: 'PREGUNTA14.png',
    15: 'PREGUNTA15.png',
    16: 'PREGUNTA16.png',
    17: 'PREGUNTA17.png',
    18: 'PREGUNTA18.png',
    19: 'PREGUNTA19.png',
    20: 'PREGUNTA20.png',
    21: 'PREGUNTA21.png',
    22: 'PREGUNTA22.png',
    23: 'PREGUNTA23.png',
    24: 'PREGUNTA24.png',
    25: 'PREGUNTA25.png',
    26: 'PREGUNTA26.png',
    27: 'PREGUNTA27.png',
    28: 'PREGUNTA28.png',
    29: 'PREGUNTA29.png',
    30: 'PREGUNTA30.png',
    31: 'PREGUNTA31.png',
    32: 'PREGUNTA32.png',
    33: 'PREGUNTA33.png',
    34: 'PREGUNTA34.png',
    35: 'PREGUNTA35.png',
    36: 'PREGUNTA36.png',
    37: 'PREGUNTA37.png',
    38: 'PREGUNTA38.png',
    39: 'PREGUNTA39.png',
    40: 'PREGUNTA39.png'
}

options = {
    1: 'RESPUESTA1.png',
    2: 'RESPUESTA2.png',
    3: 'RESPUESTA3.png',
    4: 'RESPUESTA4.png',
    5: 'RESPUESTA5.png',
    6: 'RESPUESTA6.png',
    7: 'RESPUESTA7.png',
    8: 'RESPUESTA8.png',
    9: 'RESPUESTA9.png',
    10: 'RESPUESTA10.png',
    11: 'RESPUESTA11.png',
    12: 'RESPUESTA12.png',
    13: 'RESPUESTA13.png',
    14: 'RESPUESTA14.png',
    15: 'RESPUESTA15.png',
    16: 'RESPUESTA16.png',
    17: 'RESPUESTA17.png',
    18: 'RESPUESTA18.png',
    19: 'RESPUESTA19.png',
    20: 'RESPUESTA20.png',
    21: 'RESPUESTA21.png',
    22: 'RESPUESTA22.png',
    23: 'RESPUESTA23.png',
    24: 'RESPUESTA24.png',
    25: 'RESPUESTA25.png',
    26: 'RESPUESTA26.png',
    27: 'RESPUESTA27.png',
    28: 'RESPUESTA28.png',
    29: 'RESPUESTA29.png',
    30: 'RESPUESTA30.png',
    31: 'RESPUESTA31.png',
    32: 'RESPUESTA32.png',
    33: 'RESPUESTA33.png',
    34: 'RESPUESTA34.png',
    35: 'RESPUESTA35.png',
    36: 'RESPUESTA36.png',
    37: 'RESPUESTA37.png',
    38: 'RESPUESTA38.png',
    39: 'RESPUESTA39.png',
    40: 'RESPUESTA40.png'
}

def show_questionnaire():
    st.title("Cuestionario de IQ")
    st.write("Por favor responde las siguientes preguntas:")

    responses = {}  # Diccionario para almacenar las respuestas del usuario
    for key in range(1, 41):  # Iterar sobre 40 preguntas
        question_image_path = questions.get(key)
        if question_image_path:
            # Leer la imagen de la pregunta
            with open(question_image_path, 'rb') as f:
                question_image_bytes = f.read()

            # Mostrar la imagen de la pregunta
            st.image(Image.open(io.BytesIO(question_image_bytes)), caption=f"Pregunta {key}")

        options_image_path = options.get(key)
        if options_image_path:
            # Leer la imagen de las opciones
            with open(options_image_path, 'rb') as f:
                options_image_bytes = f.read()

            # Mostrar la imagen de las opciones
            st.image(Image.open(io.BytesIO(options_image_bytes)), caption=f"Opciones {key}")

        # Obtener la respuesta del usuario
        selected_option = st.radio(f"Selecciona una opción para la pregunta {key}:", ["a", "b", "c", "d", "e", "f"],
                                   key=key)
        responses[key] = selected_option

    st.write("Respuestas:", responses)


show_questionnaire()

