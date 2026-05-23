import streamlit as st

import pickle

import numpy as np

model=pickle.load(open('lr.sav','rb'))

st.title('Sales Prediction App')

# Input Features

 

TV=st.number_input('TV adv budget', min_value=0.0)

Radio=st.number_input('Radio Adv Budget', min_value=0.0)

Newspaper=st.number_input('newpaper budget', min_value=0.0)

if st.button('predct sales'):

  input_data=np.array([[TV,Radio,Newspaper]])

  Predction=model.predict(input_data)[0]

  st.success(f'predicted Sales: {Predction:.2f}')
