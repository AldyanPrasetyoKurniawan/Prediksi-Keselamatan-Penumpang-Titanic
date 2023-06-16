import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('prediksi_keselamatan_1.sav', 'rb'))

# judul web
st.title('Prediksi Keselamatan')
st.text('Aldyan Prasetyo - 201351010 - Malam A')

Pclass = st.number_input('Pclass')

Sex = st.number_input('Sex')

SibSp = st.number_input('SibSp')

Parch = st.number_input('Parch')

Fare = st.number_input('Fare')

# code for prediction
Penumpang = ''

if st.button ('Prediksi Keselamatan') :
    Penumpang = model.predict([[Pclass, Sex, SibSp, Parch, Fare]])
    
    if (Penumpang[0]==1):
        Penumpang = 'Penumpang Selamat'
    else:
        Penumpang = 'Penumpang Tidak Selamat'
        
st.success(Penumpang)
