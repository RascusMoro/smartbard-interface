import streamlit as st
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
import os

img_path = Path(Path.cwd(), 'img')

state = os.getenv('STATE')
if state == None:
    os.environ['STATE'] = (state := 'home')

try:
    if state == 'home':

        ############## ⬇️ HOME PAGE GOES HERE ⬇️ ###############

        # Logo and other content here




        if image := st.file_uploader('', key=2, label_visibility='collapsed'):
            st.image(image, width= 600)

            suffix = Path(image.name).suffix
            with NamedTemporaryFile(delete=False, suffix=suffix, dir=img_path) as tmp:
                shutil.copyfileobj(image, tmp)
                tmp_path = Path(tmp.name)
                os.environ['IMG'] = str(tmp_path)

            if st.button('Generate limerick'):
                os.environ['STATE'] = (state := 'subpage')
                st.experimental_rerun()

    else:
        image = os.getenv('IMG')

        ############## ⬇️ SECOND PAGE GOES HERE ⬇️ ###############



        if st.button('Generate another limerick'):
            os.environ['STATE'] = (state := 'home')
            st.experimental_rerun()

except Exception as e:
    os.environ['STATE'] = 'home'
    try:
        st.experimental_rerun()
    except:
        st.error('A fatal error has occurred. Please reload the page.', icon="😱")
