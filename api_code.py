import streamlit as st
import requests

image = st.file_uploader('Choose a file', key=2)

files = {'upload_file': image}

if st.button("Generate limerick"):
    if image is not None:
        res = requests.post("http://localhost:8000/generate", files=files)
        limerick = res.json()['limerick']
        st.write(limerick)
