#Import libraries
from dotenv import load_dotenv
load_dotenv() ##Loading env variables

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load Gemini and Gemini pro model and get response
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)    
    return response.text

#Create Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input=st.text_input("Input Prompt:",key="input")

#File upload
upload_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("Tell me about the image")  

#If submit clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)