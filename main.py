### Integrate our code with OpenAPI key

import os 
from constants import openapi_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openapi_key

st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want to ")

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm(input_text))


