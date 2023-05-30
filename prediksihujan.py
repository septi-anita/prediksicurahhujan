import streamlit as st
#from PIL import Image
import numpy as np
import pandas as pd

st.set_page_config(page_title="300300", page_icon="🧊", initial_sidebar_state="expanded", layout="wide")#, theme="dark")

#image = Image.open('sunrise.jpg')

#st.image(image, caption="")

st.title("Prediksi Curah Hujan")
st.write("Developed by ")

#input date
date=st.date_input("Pick a Date")
#d=date[3]


d = date.split("-")[2]
st.write (d)  # Output: 30

#m=
#y=

tombol=st.button("cari")
if tombol:
  st.snow ()
  st.write (date)
 ####
 



