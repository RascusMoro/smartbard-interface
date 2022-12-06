#importing packages

import streamlit as st

import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image





#set page layout to wide and set page title
im = Image.open('placeholder_logo_smartbard.png')
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
components.html(
"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<link href="https://fonts.cdnfonts.com/css/simple-brush-script" rel="stylesheet">



<style>
@font-face {
  font-family: simple brush script; src: url("https://fonts.cdnfonts.com/css/simple-brush-script")}
<!--@import url('https://fonts.cdnfonts.com/css/simple-brush-script');-->


.bg-light {

    padding-left: 0rem;
    padding-right: 0rem;
    overflow: hidden;
    background-color: #FFFFFF !important;}
</style>

    <!-- bg-light -->

<!-- Image and text -->
<nav class="navbar navbar-light bg-light">
  <div class="container-fluid">

    <a class="navbar-brand">
      <img src="https://i.ibb.co/h8LQxrp/Placeholder-Logo-Smart-Bard.png" class="me-2" height="50"/>
      <big>
        <span style= "font-family: 'Brush Script MT'">SmartBard</span>
      </big>
    </a>

    <a >
      <h2 class="navbar-description">
        <span style= "font-family: 'Brush Script MT'">Give us an image and we will turn it into a poem</span>
        </h2>
    </a>

  </div>
</nav>
""")


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
