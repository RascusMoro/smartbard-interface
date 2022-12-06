#importing packages

import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image
import pickle as pkle
import os.path
import frontend


#set page layout to wide and set page title
im = Image.open('/Users/sebastian/code/rcfeord/smartbard-api/frontend/images/SmartBard_Logo_Updated.png')
st.set_page_config(layout="wide", page_title="SmartBard", page_icon = im)

#Remove the Menu Button and Streamlit Icon
hide_default_format = """
       <style>
    #MainMenu {visibility: visible; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# hide fullsize button
hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''
st.markdown(hide_img_fs, unsafe_allow_html=True)





uploaded_file = frontend.app.a_file()

@st.experimental_memo
def b_file():
    return uploaded_file

st.image(b_file(), caption="test")
