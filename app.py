#Import libraries
from dotenv import load_dotenv
load_dotenv() ##Loading env variables
import os

import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load Gemini and Gemini pro model and get response
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#Intilialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

#When Submit clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)