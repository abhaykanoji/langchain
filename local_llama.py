from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question: {question}")
    ]
)

st.title("ollama")
input_text = st.text_input("enter your query: ")

llm = Ollama(model="llama3")
output_parse = StrOutputParser()
chain = prompt | llm | output_parse
# chain = prompt,llm,output_parse

if input_text:
    st.write(chain.invoke({'question':input_text}))