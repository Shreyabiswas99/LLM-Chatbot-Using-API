from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

App = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A basic API server"
)

add_routes(
    App,
    ChatOpenAI(),
    path = "/openai"
)

Model = ChatOpenAI()
LLM = Ollama(model = "llama3.2")

Prompt1 = ChatPromptTemplate.from_template("Write a speech on {topic} in 100 words")
Prompt2 = ChatPromptTemplate.from_template("Write a poem on {topic} in 100 words")

add_routes(
    App,
    Prompt1|Model,
    path = "/speech"
)

add_routes(
    App,
    Prompt2|LLM,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run (App, host="localhost", port=8000)