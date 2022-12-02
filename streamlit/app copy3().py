#importing packages

import streamlit as st

import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image





#set page layout to wide and set page title
im = Image.open('/Users/sebastian/code/rcfeord/smartbard/streamlit/.streamlit/images/SmartBard_Logo_Updated.png')
st.set_page_config(layout="wide", page_title="SmartBard", page_icon = im)

#Remove the Menu Button and Streamlit Icon
hide_default_format = """
       <style>
    #MainMenu {visibility: visible; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''
st.markdown(hide_img_fs, unsafe_allow_html=True)

#Navbar with logo


image1 = Image.open('/Users/sebastian/code/rcfeord/smartbard/streamlit/.streamlit/images/SmartBard_Logo_Updated.png')

st.image(image1, width= 800)

image2 = Image.open('/Users/sebastian/code/rcfeord/smartbard/streamlit/.streamlit/images/SmartBard_Header_Text.png')

st.image(image2, width= 800)


col4, col5 = st.columns(2)


#upload image
with col4:


    holder = st.empty()
    uploaded_file = st.file_uploader('Choose a file', key=2)

# if no image is uploaded: empty text area
    if uploaded_file is None:
        with col5:
            st.text_area(label ="This will be the output", height =400)

# if image is uploaded: the upload window closes and the image is displayed
    elif uploaded_file is not None:
        st.image(uploaded_file)
        #holder.empty()
        with col5:

# display the poem on the right side

            st.text_area('Write some text', '''Some diseases by which we're attacked
Can be monitored, followed and tracked.
When a clear biomarker
Gets lighter or darker,
We're better or worse—that's a fact!''', height=600, disabled=True)


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

if uploaded_file is not None:

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
            file_name='placeholder_logo_smartbard.png',
            #mime='text/csv',
        )

    with col10:
        st.write('')

    with col11:
        st.write('')

    with col12:
        st.write('')
