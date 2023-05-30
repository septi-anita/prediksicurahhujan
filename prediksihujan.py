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

#input place
###########################################
df = pd.read_csv(r'data_hujan.csv')
kt = df[1]
kota = st.selectbox ("Pilih lokasi anda:", kt)

###########################################
#df = pd.read_csv(r'.csv')
#place = st.selectbox ("Pilih lokasi anda:", df)

tombol=st.button("cari")
if tombol:
  st.snow ()
  #CH= df[1][kota]
  #st.write (CH)
 ####
 



