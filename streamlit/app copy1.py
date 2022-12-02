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




components.html(
"""



<style>
 img {
    width: 70px;
    float: right;
    margin-right: 10px;
  }
  div {
  text-align: center;
  border: 3px solid black;
  font-family: cursive;
}


</style>

<img src="https://benedictraven.co.uk/wp-content/uploads/2021/04/Feather.jpg" />
<div>
  <h1>SmartBard</h1>
</div>



""")



#logo
components.html(
"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    <nav class="navbar bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="https://benedictraven.co.uk/wp-content/uploads/2021/04/Feather.jpg" alt="Logo" width="50" height="50" class="d-inline-block align-text-center">
      SmartBard
    </a>
  </div>
</nav>

""")

#<img src="https://benedictraven.co.uk/wp-content/uploads/2021/04/Feather.jpg" alt="Logo" width="100" height="100">

    #st.image("placeholder_logo_smartbard.png", width=100)
#description

"""
Give us an image an we will turn it into a poem
"""

col4, col5 = st.columns(2)



with col4:


    holder = st.empty()
    uploaded_file = holder.file_uploader('Choose a file', key=2)


    if uploaded_file is not None:
        st.image(uploaded_file)
        holder.empty()





#modelresponse = model_function(input)

with col5:
    st.text_area(label ="This will be the output", height =400)







#if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    #dataframe = pd.read_csv(uploaded_file)
    #st.write(dataframe)
