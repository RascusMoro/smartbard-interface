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

# set images
icon = Image.open(Path(assets_path, 'feather_with_background.png'))
logo = Image.open(Path(assets_path, 'SmartBard_Logo_Updated.png'))
header = Image.open(Path(assets_path, 'SmartBard_Header_Text.png'))

if 'state' not in st.session_state:
    st.session_state.state = 'home'

if 'img' not in st.session_state:
    st.session_state.img = None

if 'limerick' not in st.session_state:
    st.session_state.limerick = ''

if 'layout' not in st.session_state:
    st.session_state.layout = 'centered'

st.set_page_config(layout=st.session_state.layout, page_title="SmartBard", page_icon=icon)

#Remove the Menu Button and Streamlit Icon
hide_default_format = """
    <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_default_format, unsafe_allow_html=True)

# hide fullsize button
hide_img_fs = '''
    <style>
        button[title="View fullscreen"] {
            visibility: hidden;
        }
        .css-1j77i4l {
            display: flex;
            justify-content: center;
        }
        .css-keje6w {
            display: flex;
            align-items: center;
        }
    </style>
    '''
st.markdown(hide_img_fs, unsafe_allow_html=True)

# Remove whitespace from the top of the page
remove_w_s = '''
        <style>
                div.block-container {
                    padding-top:1rem;
                    padding-bottom:0rem;
                }
        </style>
        '''
st.markdown(remove_w_s, unsafe_allow_html=True)


try:
    if st.session_state.state == 'home':

        ############## ⬇️ HOME PAGE GOES HERE ⬇️ ###############
        st.image(logo, width= 700)
        st.image(header, width= 700)

        if image := st.file_uploader('', type=['png', 'jpg', 'jpeg'], label_visibility='collapsed'):

            col_left, col_center, col_right = st.columns([5,3,5])

            with col_center:
                st.image(image)
                st.write(" ")
                st.write(" ")

            button_col_left, button_col_center, button_col_right = st.columns([5,8,5])

            with button_col_center:

                if st.button('Generate limerick'):

                    # show spinning wheel
                    with open(Path(assets_path, "loading.gif"), "rb") as f:
                        contents = f.read()
                        data_url = base64.b64encode(contents).decode("utf-8")
                    st.markdown(
                        f'<img style="width: 50px;" src="data:image/gif;base64,{data_url}">',
                        unsafe_allow_html=True,
                    )

                    st.session_state.img = image
                    file = image.getbuffer()
                    files = {'upload_file': file}
                    try:
                        # call the API
                        if file is not None:
                            # res = requests.post("https://backend-iy6puqsg3a-ew.a.run.app/generate", files=files)
                            # st.session_state.limerick = res.json()['limerick']
                            st.session_state.limerick = 'limerick'

                        # set new state to subpage and layout to wide
                        st.session_state.state = 'subpage'
                        st.session_state.layout = 'wide'

                        # if res.status_code != 200:
                        #     raise Exception('Bad response code')


                    except Exception as e:
                        # st.write(e)
                        st.write('Something went wrong. Please try again!')
                        time.sleep(3)

                    st.experimental_rerun()


    else:
        image = st.session_state.img
        limerick = st.session_state.limerick

        ############## ⬇️ SECOND PAGE GOES HERE ⬇️ ###############
        st.image(logo, width= 200)

        col_picture, col_text = st.columns(2)
        rcol_left, rcol_center, rcol_right = st.columns([5,3,5])

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
                # set new state to home and layout to centered
                st.session_state.state = 'home'
                st.session_state.layout = 'centered'


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
    st.session_state.state = 'home'
    try:
        st.experimental_rerun()
    except:
        st.exception(e)
        st.error('A fatal error has occurred. Please reload the page.', icon="😱")
finally:
    pass

####
