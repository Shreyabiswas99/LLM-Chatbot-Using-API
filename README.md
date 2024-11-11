# Production Grade Deployment LLM as API Using LangChain and FastAPI
* Inside this project we have built an LLM Chatbot like the previous simple LLM chatbot but in this we deployed our LLM model as an API Server
* LangServe helps developers deploy LangChain runnables and chains as a REST API. This library is integrated with FastAPI and uses pydantic for data validation.
* In addition, it provides a client that can be used to call into runnables deployed on a server. A JavaScript client is available in LangChain.js.
## Setup
* If using VSCode make sure to setup the environment for our model, we can do that by running this command on the terminal : create -p venv python=3.9 -y
* Activate it by using conda activate venv
* Make sure you have latest version of python and VSCode setup
* Lastly install all the required libraries by running pip install -r requirements.txt
## Running 
* Run the LLM model using Streamlit by using streamlit run filename
