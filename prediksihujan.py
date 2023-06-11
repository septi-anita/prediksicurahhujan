import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime 
#import calendar as cld

st.set_page_config(page_title="AI:RainfallPrediction", page_icon="🧊", initial_sidebar_state="collapsed", layout="centered")#, theme="dark")

#Gambar
col1, col2, col3 = st.columns([0.55, 0.1, 0.35])

with col1:
    st.title("Rainfall Prediction AI")
    st.write("Developed by Z.L.D.S Team")

with col2:
    st.write('       ')
    
with col3:
    image = Image.open('Rainy Weather (HD).png')
    st.image(image, caption=None, width=300)


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

#read data
df = pd.read_csv(r'data_hujan.csv')

PCHMAR23 = df[3][D]
#PCHAPR23 = df[4][D+1]
#PCHMEI23 = df[5][D+1] #kolom pertama "No." sementara diasumsikan sebagai tanggal

#CH = (PCHMAR23+PCHAPR23+PCHMEI23)/3

tombol=st.button("search")
if tombol:
  #st.write (CH)
  #st.snow ()
  st.write (date)
  image = Image.open('hujan deras.png')
  st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
  st.write ('hujan deras')
 
  #tmpilan harian 
  #if CH>=168:
      #st.write(D+1)
      #image = Image.open('hujan deras.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('hujan deras')
   #elif CH in range (82, 168):
      #st.write(D+1)
      #image = Image.open('gerimis.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('gerimis')
   #else:
      #st.write(D+1)
      #image = Image.open('tidak hujan.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('tidak hujan')
    
  #tampilan sebulan  
  #for D in range (0,30):
    #if CH>=168:
      #st.write(D+1)
      #image = Image.open('hujan deras.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('hujan deras')
    #elif CH<=168 and CH>=82:
      #st.write(D+1)
      #image = Image.open('gerimis.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('gerimis')
    #else :
      #st.write(D+1)
      #image = Image.open('tidak hujan.png')
      #st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #st.write ('tidak hujan')
 
  #col1, col2, col3 = st.columns(3)

  #with col1:
   #st.header("A cat")
   #st.image("https://static.streamlit.io/examples/cat.jpg")



