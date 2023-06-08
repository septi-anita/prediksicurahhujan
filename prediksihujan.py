import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime 
#import calendar as cld

st.set_page_config(page_title="300300", page_icon="🧊", initial_sidebar_state="expanded", layout="wide")#, theme="dark")

image = Image.open('Rainy Weather (HD).png')

st.image(image, caption="yy")

st.title("Prediksi Curah Hujan")
st.write("Developed by Z.L.D.S Team")

#input date
date=st.date_input("Pick a Date")

Y= date.strftime("%Y")
Y=int(Y)
#st.write(Y)

M= date.strftime("%m")
M=int(M)
#st.write(M)

D= date.strftime("%d")
D=int(D)
#st.write(D)

tombol=st.button("cari")
if tombol:
  st.snow ()
  st.write (date)

 



