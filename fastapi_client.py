import streamlit as st
import requests

def ollama_resp(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json = {'input':{"topic":input_text}})
    
    return response.json()['output']

st.title("langchain ollama llama3")
input_text = st.text_input("write topic")

if input_text:
    st.write(ollama_resp(input_text))   