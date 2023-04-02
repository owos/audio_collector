import os
import numpy as np
import streamlit as st
import random
from io import BytesIO
import streamlit.components.v1 as components
  
from st_custom_components import st_audiorec

# Python3 code to generate
# id using uuid4()
  
import uuid
  
id = uuid.uuid4()
age_group = st.selectbox("Age group", options= ["","<19", "19-29", "30-39","40-49", "50-59", ">59"])
gender = st.selectbox("Gender", options= ["","Female", "Male"])
accent = st.selectbox("Accent*", options= ["","Hull", "Others"])
country = st.selectbox("Country", options= ["","UK", "Others"])

with open('cv-valid-test.txt', 'r') as f:
    line   = f.readlines()

index =random.sample(line, 1)[0]

with st.expander('', expanded=True):
    st.markdown(f'''
    ##### Record the text below
    <ul style="padding-left:20px">
      <h4> {index} </h4>
      </li>
      
    </ul>
    ''', unsafe_allow_html=True)
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # display audio data as received on the backend
    #st.audio(wav_audio_data, format='audio/wav')
    pass
    
# INFO: by calling the function an instance of the audio recorder is created
# INFO: once a recording is completed, audio data will be saved to wav_audio_data