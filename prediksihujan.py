import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="300300", page_icon="🧊", initial_sidebar_state="expanded", layout="wide")#, theme="dark")

#audio_file = open('myaudio.ogg', 'rb')
#audio_bytes = audio_file.read()

#st.audio(audio_bytes, format='audio/ogg')

#image = Image.open('sunrise.jpg')

#st.image(image, caption="I'm one of the luckiest person cause I have friend like u")
st.balloons()
st.title("Prediksi Curah Hujan")
st.write("Developed by ")
date=st.date_input("pick a date")
tombol=st.button("pencet sini")
if tombol:
 st.balloons()
 



