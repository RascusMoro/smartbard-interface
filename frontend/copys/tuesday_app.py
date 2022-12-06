#importing packages

import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image
import pickle as pkle
import os.path
import webbrowser





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



# Three columns to center
col1, col2, col3 = st.columns([1, 3, 1])

# display the logo and description
with col2:

    image1 = Image.open('/Users/sebastian/code/rcfeord/smartbard-api/frontend/images/SmartBard_Logo_Updated.png')

    a = st.image(image1, width= 700)

    image2 = Image.open('/Users/sebastian/code/rcfeord/smartbard-api/frontend/images/SmartBard_Header_Text.png')

    b = st.image(image2, width= 700)





#upload image
    if 'file' not in st.session_state:
        st.session_state['file'] = None
    st.session_state['file'] = st.file_uploader('Choose a file')


 #or whatever default
#UPLOADED_FILE = st.session_state['file']


#if image is uploaded: the upload window closes and the image is displayed


col_picture, col_text = st.columns(2)



#if UPLOADED_FILE is not None:
 #   @st.experimental_memo
  #  def a_file():
   #     file = UPLOADED_FILE
    #    return file

    #with col_picture:
     #   webbrowser.open('http://localhost:8501/display_demo')  # Go to example.com
      #  st.image(UPLOADED_FILE, caption="test")

# display the poem on the right side
with col_text:
        st.text_area("test",
    '''Some diseases by which we're attacked
Can be monitored, followed and tracked.
When a clear biomarker
Gets lighter or darker,
We're better or worse—that's a fact!''', height=600, disabled=True, label_visibility='collapsed')


        # Add css to make text bigger
        st.markdown(
                        """
                        <style>

                        textarea {
                            font-size: 40px !important;
                            font-family: 'Brush Script MT' !important;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True,
                        )
# if the image is uploaded: add a download button
if st.session_state['file'] is not None:

    col6, col7, col8, col9, col10, col11, col12 = st.columns(7)
    with col6:
            st.write('')

    with col7:
        st.write('')

    with col8:
        st.write('')

    with col9:
        df = pd.DataFrame(["test"])

        @st.cache
        def convert_df(df):
            #IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)
            #Download
        st.download_button(
            label="Download Your Poem",
            data=csv,
            file_name='/Users/sebastian/code/rcfeord/smartbard-api/frontend/images/placeholder_logo_smartbard.png',
            #mime='text/csv',
        )

    with col10:
        st.write('')

    with col11:
        st.write('')

    with col12:
        st.write('')

st.session_state['file'].sync()
