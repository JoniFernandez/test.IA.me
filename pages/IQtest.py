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


questions = {1: '/Users/josefinafernandez/Desktop/PREGUNTA1.png',
             2: '/Users/josefinafernandez/Desktop/PREGUNTA2.png',
             3: '/Users/josefinafernandez/Desktop/PREGUNTA3.png',
             4: '/Users/josefinafernandez/Desktop/PREGUNTA4.png',
             5: '/Users/josefinafernandez/Desktop/PREGUNTA5.png',
             6: '/Users/josefinafernandez/Desktop/PREGUNTA6.png',
             7: '/Users/josefinafernandez/Desktop/PREGUNTA7.png',
             8: '/Users/josefinafernandez/Desktop/PREGUNTA8.png',
             9: '/Users/josefinafernandez/Desktop/PREGUNTA9.png',
             10: '/Users/josefinafernandez/Desktop/PREGUNTA10.png',
             11: '/Users/josefinafernandez/Desktop/PREGUNTA11.png',
             12: '/Users/josefinafernandez/Desktop/PREGUNTA12.png',
             13: '/Users/josefinafernandez/Desktop/PREGUNTA13.png',
             14: '/Users/josefinafernandez/Desktop/PREGUNTA14.png',
             15: '/Users/josefinafernandez/Desktop/PREGUNTA15.png',
             16: '/Users/josefinafernandez/Desktop/PREGUNTA16.png',
             17: '/Users/josefinafernandez/Desktop/PREGUNTA17.png',
             18: '/Users/josefinafernandez/Desktop/PREGUNTA18.png',
             19: '/Users/josefinafernandez/Desktop/PREGUNTA19.png',
             20: '/Users/josefinafernandez/Desktop/PREGUNTA20.png',
             21: '/Users/josefinafernandez/Desktop/PREGUNTA21.png',
             22: '/Users/josefinafernandez/Desktop/PREGUNTA22.png',
             23: '/Users/josefinafernandez/Desktop/PREGUNTA23.png',
             24: '/Users/josefinafernandez/Desktop/PREGUNTA24.png',
             25: '/Users/josefinafernandez/Desktop/PREGUNTA25.png',
             26: '/Users/josefinafernandez/Desktop/PREGUNTA26.png',
             27: '/Users/josefinafernandez/Desktop/PREGUNTA27.png',
             28: '/Users/josefinafernandez/Desktop/PREGUNTA28.png',
             29: '/Users/josefinafernandez/Desktop/PREGUNTA29.png',
             30: '/Users/josefinafernandez/Desktop/PREGUNTA30.png',
             31: '/Users/josefinafernandez/Desktop/PREGUNTA31.png',
             32: '/Users/josefinafernandez/Desktop/PREGUNTA32.png',
             33: '/Users/josefinafernandez/Desktop/PREGUNTA33.png',
             34: '/Users/josefinafernandez/Desktop/PREGUNTA34.png',
             35: '/Users/josefinafernandez/Desktop/PREGUNTA35.png',
             36: '/Users/josefinafernandez/Desktop/PREGUNTA36.png',
             37: '/Users/josefinafernandez/Desktop/PREGUNTA37.png',
             38: '/Users/josefinafernandez/Desktop/PREGUNTA38.png',
             39: '/Users/josefinafernandez/Desktop/PREGUNTA39.png',
             40: '/Users/josefinafernandez/Desktop/PREGUNTA39.png' }

options = {1: '/Users/josefinafernandez/Desktop/RESPUESTA1.png',
           2: '/Users/josefinafernandez/Desktop/RESPUESTA2.png',
           3: '/Users/josefinafernandez/Desktop/RESPUESTA3.png',
             4: '/Users/josefinafernandez/Desktop/RESPUESTA4.png',
             5: '/Users/josefinafernandez/Desktop/RESPUESTA5.png',
             6: '/Users/josefinafernandez/Desktop/RESPUESTA6.png',
             7: '/Users/josefinafernandez/Desktop/RESPUESTA7.png',
             8: '/Users/josefinafernandez/Desktop/RESPUESTA8.png',
             9: '/Users/josefinafernandez/Desktop/RESPUESTA9.png',
             10: '/Users/josefinafernandez/Desktop/RESPUESTA10.png',
             11: '/Users/josefinafernandez/Desktop/RESPUESTA11.png',
             12: '/Users/josefinafernandez/Desktop/RESPUESTA12.png',
             13: '/Users/josefinafernandez/Desktop/RESPUESTA13.png',
             14: '/Users/josefinafernandez/Desktop/RESPUESTA14.png',
             15: '/Users/josefinafernandez/Desktop/RESPUESTA15.png',
             16: '/Users/josefinafernandez/Desktop/RESPUESTA16.png',
             17: '/Users/josefinafernandez/Desktop/RESPUESTA17.png',
             18: '/Users/josefinafernandez/Desktop/RESPUESTA18.png',
             19: '/Users/josefinafernandez/Desktop/RESPUESTA19.png',
             20: '/Users/josefinafernandez/Desktop/RESPUESTA20.png',
             21: '/Users/josefinafernandez/Desktop/RESPUESTA21.png',
             22: '/Users/josefinafernandez/Desktop/RESPUESTA22.png',
             23: '/Users/josefinafernandez/Desktop/RESPUESTA23.png',
             24: '/Users/josefinafernandez/Desktop/RESPUESTA24.png',
             25: '/Users/josefinafernandez/Desktop/RESPUESTA25.png',
             26: '/Users/josefinafernandez/Desktop/RESPUESTA26.png',
             27: '/Users/josefinafernandez/Desktop/RESPUESTA27.png',
             28: '/Users/josefinafernandez/Desktop/RESPUESTA28.png',
             29: '/Users/josefinafernandez/Desktop/RESPUESTA29.png',
             30: '/Users/josefinafernandez/Desktop/RESPUESTA30.png',
             31: '/Users/josefinafernandez/Desktop/RESPUESTA31.png',
             32: '/Users/josefinafernandez/Desktop/RESPUESTA32.png',
             33: '/Users/josefinafernandez/Desktop/RESPUESTA33.png',
             34: '/Users/josefinafernandez/Desktop/RESPUESTA34.png',
             35: '/Users/josefinafernandez/Desktop/RESPUESTA35.png',
             36: '/Users/josefinafernandez/Desktop/RESPUESTA36.png',
             37: '/Users/josefinafernandez/Desktop/RESPUESTA37.png',
             38: '/Users/josefinafernandez/Desktop/RESPUESTA38.png',
             39: '/Users/josefinafernandez/Desktop/RESPUESTA39.png',
             40: '/Users/josefinafernandez/Desktop/RESPUESTA40.png'}


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

