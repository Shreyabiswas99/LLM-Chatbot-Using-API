import requests
import streamlit as st

def openai_getrequest(input_text):
    response=requests.post("http://localhost:8000/speech/invoke",
    json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def ollama_getrequest(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})
    return response.json()['output']

st.title("Langchain API Server Demo")
input_text = st.text_input("Write a speech on ")
input_text1 = st.text_input("Write a poem on ")

if input_text:
    st.write(openai_getrequest(input_text))

if input_text:
    st.write(ollama_getrequest(input_text1))