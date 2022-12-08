import streamlit as st
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
import os
import requests
import numpy as np
import pandas as pd
from PIL import Image
import pickle as pkle
import streamlit.components.v1 as components



# img_path = Path(Path.cwd(), 'img_tmp')
# img_path = '/app/smartbard-api/img_tmp'
img_path = 'img_tmp'

state = os.getenv('STATE')
if state == None:
    os.environ['STATE'] = (state := 'home')

try:
    if state == 'home':

        ############## ⬇️ HOME PAGE GOES HERE ⬇️ ###############


        #set page layout to wide and set page title
        # im = Image.open('/app/smartbard-api/SmartBard_Logo_Updated.png')
        im = Image.open('SmartBard_Logo_Updated.png')
        #im = Image.open('/Users/sebastian/code/rcfeord/smartbard-api/frontend/images/SmartBard_Logo_Updated.png')
        st.set_page_config(layout="centered", page_title="SmartBard", page_icon = im)

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


        # Logo and other content here
        # Three columns to center
        #col1, col2, col3 = st.columns(3)

        #with col1: ""

# display the logo and description
        #with col2:

        # image1 = Image.open('/app/smartbard-api/SmartBard_Logo_Updated.png')
        image1 = Image.open('SmartBard_Logo_Updated.png')

        a = st.image(image1, width= 700)

        # image2 = Image.open('/app/smartbard-api/SmartBard_Header_Text.png')
        image2 = Image.open('SmartBard_Header_Text.png')


        b = st.image(image2, width= 700)

        #with col3: ""


        if image := st.file_uploader('', key=2, label_visibility='collapsed'):
            col_left1, col_left2, col_left3, col_left4, col_left5, col_center, col_right1, col_right2, col_right3, col_right4, col_right5 = st.columns([1,1,1,1,1,3,1,1,1,1,1])

            with col_center:
                st.image(image)

                suffix = Path(image.name).suffix
                with NamedTemporaryFile(delete=False, suffix=suffix, dir=img_path) as tmp:
                    shutil.copyfileobj(image, tmp)
                    tmp_path = Path(tmp.name)
                    os.environ['IMG'] = str(tmp_path)

                st.write(" ")
                st.write(" ")
            button_col_left1, button_col_left2, button_col_left3, button_col_left4, button_col_left5, button_col_center, button_col_right1, button_col_right2, button_col_right3, button_col_right4, button_col_right5 = st.columns([1,1,1,1,1,8,1,1,1,1,1])

            with button_col_center:
                if st.button('Generate limerick'):
                        os.environ['STATE'] = (state := 'subpage')
                        st.experimental_rerun()

    else:
        image = os.getenv('IMG')

        ############## ⬇️ SECOND PAGE GOES HERE ⬇️ ###############


        #set page layout to wide and set page title
        # im = Image.open('/app/smartbard-api/SmartBard_Logo_Updated.png')
        im = Image.open('SmartBard_Logo_Updated.png')
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




        col_picture, col_text = st.columns(2)
        rcol_left1, rcol_left2, rcol_left3, rcol_left4, rcol_left5, rcol_center, rcol_right1, rcol_right2, rcol_right3, rcol_right4, rcol_right5, = st.columns([1,1,1,1,1,3,1,1,1,1,1])


        if image is not None:
                # im = cv2.imread(image)
                with col_picture:
                    #pyautogui.hotkey('f5')
                    st.image(image, width=600)


                with col_text:
                        st.text(
                    '''Some diseases by which we're attacked \nCan be monitored, followed and tracked. \nWhen a clear biomarker \nGets lighter or darker, \nWe're better or worse—that's a fact!''')

# Add css to make text bigger
                st.markdown(
                            """
                            <style>

                            text {
                                font-size: 80px !important;
                                font-family: 'Brush Script MT' !important;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True,
                            )





        with rcol_center:
            st.write(" ")
            st.write(" ")
            if st.button('Generate another limerick'):
                os.environ['STATE'] = (state := 'home')
                st.experimental_rerun()
# -------------------------------------------------------------------
    m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #fccf03;
    color:#012C49;
    font-family: Helvetica;
    width: 300px;
    height: 40px;
}
div.stButton > button:hover {
    background-color: #fccf03;
    color:#006CC3;
    font-family: sans-serif
    }

div.stText {
    text-align: center;
    font-size: 300px !important;


}
</style>""", unsafe_allow_html=True)


# -------------------------------------------------------------------


except Exception as e:
    os.environ['STATE'] = 'home'
    try:
        st.experimental_rerun()
    except:
        st.exception(e)
        st.error('A fatal error has occurred. Please reload the page.', icon="😱")

####