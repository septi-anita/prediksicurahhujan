import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime 
#import calendar as cld

st.set_page_config(page_title="300300", page_icon="🧊", initial_sidebar_state="expanded", layout="wide")#, theme="dark")

#Gambar
col1, col2, = st.columns(2)

with col1:
    st.title("Rainfall Prediction AI")
    st.write("Developed by Z.L.D.S Team")

with col2:
    image = Image.open('Rainy Weather (HD).png')
    st.image(image, caption=None, width=400)

#with col3:
    #st.write(' ')

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
  #st.snow ()
  st.write (date)
  image = Image.open('hujan deras.png')
  st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
  st.write ('hujan deras')
  
  #if :
    #image = Image.open('hujan deras.png')
    #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.write ('hujan deras')
  #elif :
    #image = Image.open('gerimis.png')
    #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.write ('gerimis')
  #else :
    #image = Image.open('tidak hujan.png')
    #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.write ('tidak hujan')
 



