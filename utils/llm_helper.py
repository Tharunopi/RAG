import streamlit as st
import time
from uuid import uuid4, UUID
from utils.atlas import mongoClient
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

template = """Answer to this question from user 
Question: {question}"""

atlas_client = mongoClient()
prompt_construction = ChatPromptTemplate.from_template(template)
chain = prompt_construction | st.session_state["large_language_model"] | StrOutputParser()

def write_msg_history() -> None:
    """Writes the chat history for a thread after each prompt input.
    """
    for i in st.session_state.messages:
        with st.chat_message(i["role"]):
            st.markdown(i["context"])

def query_to_llm(prompt:str):
   return chain.stream({"question": prompt})

def perform_chat_operations(email:str, chat_history:list[dict], operation:str, uuid:UUID=uuid4()) -> None:
    assert operation in ["insert", "append", "delete"]
    """
    It manages the insert, append and delete operation for every threads. (ie: going to insert, append or delete chat messages based on user preference)
    """
    pass 