import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime 
#import calendar as cld

st.set_page_config(page_title="AI:RainfallPrediction", page_icon="☔", initial_sidebar_state="collapsed", layout="centered")

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

V=[]

def app ():
    for i in range (1, 32):
       V.append(i)
def call ():
    global CH, D, M, Y
  
    for D in V :
       if CH>=40:
            st.write(D, M, Y)
            image = Image.open('hujan deras.png')
            st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            st.write ('hujan deras')

       elif CH<=30:
            st.write(D, M, Y)
            image = Image.open('tidak hujan.png')
            st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            st.write ('tidak hujan')
        
       else:
            st.write(D, M, Y)
            image = Image.open('gerimis.png')
            st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            st.write ('gerimis')
      

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

PCHMAR23 = df['PCHMAR23'][D-1]
PCHAPR23 = df['PCHAPR23'][D-1]
PCHMEI23 = df['PCHMEI23'][D-1] #kolom pertama "No." sementara diasumsikan sebagai tanggal

CH = (PCHMAR23+PCHAPR23+PCHMEI23)/3
#st.write(CH)


tombol=st.button("search")
if tombol:
  #tampilan harian
   st.write('This Day')
   if CH>=40:
      st.write(D, M, Y)
      image = Image.open('hujan deras.png')
      st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      st.write ('hujan deras')

   elif CH<=30:
      st.write(D, M, Y)
      image = Image.open('tidak hujan.png')
      st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      st.write ('tidak hujan')
        
   else:
      st.write(D, M, Y)
      image = Image.open('gerimis.png')
      st.image(image, caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      st.write ('gerimis')
    
   st.write ('data bulanan')

    #tampilan sebulan
    
   app()
   call()

 

# Mendapatkan jumlah kolom dari pengguna
n = st.number_input('Masukkan jumlah kolom:', min_value=1, step=1)

# Membuat data dengan kolom-kolom sesuai jumlah yang dimasukkan
data = {}
for i in range(n):
    column_name = f'Kolom {i+1}'
    column_data = [f'Data {j+1}' for j in range(5)]  # contoh data
    data[column_name] = column_data

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan tabel
st.table(df)
 
  #col1, col2, col3 = st.columns(3)

  #with col1:
   #st.header("A cat")
   #st.image("https://static.streamlit.io/examples/cat.jpg")

#ite = range(1,jh+1,1)
#for D in ite :



