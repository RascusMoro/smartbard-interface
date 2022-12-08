import streamlit as st
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
import os
import requests
from PIL import Image
import time
import base64

assets_path = 'assets'
img_path = 'img_tmp'

state = os.getenv('STATE')
if state == None:
    os.environ['STATE'] = (state := 'home')

try:
    if state == 'home':

        ############## ⬇️ HOME PAGE GOES HERE ⬇️ ###############

        #set page layout to wide and set page title

        im = Image.open(Path(assets_path, 'SmartBard_Logo_Updated.png')) #TODO: change with small icon
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

        image1 = Image.open(Path(assets_path, 'SmartBard_Logo_Updated.png'))
        a = st.image(image1, width= 700)

        image2 = Image.open(Path(assets_path, 'SmartBard_Header_Text.png'))

        b = st.image(image2, width= 700)

        if image := st.file_uploader('', key=2, label_visibility='collapsed'):
            col_left1, col_left2, col_left3, col_left4, col_left5, \
                col_center, col_right1, col_right2, col_right3, col_right4, \
                    col_right5 = st.columns([1,1,1,1,1,3,1,1,1,1,1])

            with col_center:
                st.image(image)

                suffix = Path(image.name).suffix
                with NamedTemporaryFile(delete=False, suffix=suffix, dir=img_path) as tmp:
                    shutil.copyfileobj(image, tmp)
                    tmp_path = Path(tmp.name)
                    os.environ['IMG'] = str(tmp_path)

                st.write(" ")
                st.write(" ")

            button_col_left1, button_col_left2, button_col_left3, button_col_left4, \
                button_col_left5, button_col_center, button_col_right1, button_col_right2, \
                    button_col_right3, button_col_right4, \
                        button_col_right5 = st.columns([1,1,1,1,1,8,1,1,1,1,1])

            with button_col_center:
                #files = {'upload_file': image}
                if st.button('Generate limerick'):

                    # show progress bar #TODO: fix this!
                    file_ = open(Path(assets_path, "progress_bar.gif"), "rb")
                    contents = file_.read()
                    data_url = base64.b64encode(contents).decode("utf-8")
                    file_.close()
                    st.markdown(
                        f'<img src="data:image/gif;base64,{data_url}">',
                        unsafe_allow_html=True,
                    )

                    file = open(tmp_path, 'rb')
                    files = {'upload_file': file}
                    try:
                        # call the API
                        if file is not None:
                            res = requests.post("https://backend-iy6puqsg3a-ew.a.run.app/generate", files=files)
                            os.environ['LIMERICK'] = (limerick := res.json()['limerick'])

                        # set new state to subpage
                        os.environ['STATE'] = (state := 'subpage')

                        if res.status_code != 200:
                            raise Exception('Bad response code')

                    except Exception as e:
                        # st.write(e)
                        st.write('Something went wrong. Please try again!')
                        time.sleep(5)

                    st.experimental_rerun()

    else:
        image = os.getenv('IMG')
        limerick = os.getenv('LIMERICK')

        ############## ⬇️ SECOND PAGE GOES HERE ⬇️ ###############


        #set page layout to wide and set page title
        im = Image.open(Path(assets_path, 'SmartBard_Logo_Updated.png'))
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
        rcol_left1, rcol_left2, rcol_left3, rcol_left4, rcol_left5, \
            rcol_center, rcol_right1, rcol_right2, rcol_right3, rcol_right4, \
                rcol_right5, = st.columns([1,1,1,1,1,3,1,1,1,1,1])

        if image is not None:
            # print the image
            with col_picture:
                st.image(image, width=600)
            # print the limerick
            with col_text:
                st.text(limerick)

            # Add css to make text bigger
            st.markdown(
            """
            <style>

            [data-testid="stText"] {
                font-size: 30px !important;
                font-family: Helvetica !important;
                line-height: 2;
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

                # delete all tmp images
                for filename in os.listdir(img_path):
                    file_path = os.path.join(img_path, filename)
                    os.unlink(file_path)

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
