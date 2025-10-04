import streamlit as st
import time
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

template = """Answer to this question from user 
Question: {question}"""

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