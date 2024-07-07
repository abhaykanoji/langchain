from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from fastapi import FastAPI
import uvicorn
from langserve import add_routes

app =  FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

llm = Ollama(model="llama3")
prompt = ChatPromptTemplate.from_template("write 100 word  eassy on {topic}")

add_routes(
    app,
    prompt|llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0")