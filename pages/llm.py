import streamlit as st
from utils.llm_helper import write_msg_history, query_to_llm

model_status = st.session_state["large_language_model_status"]
model = st.session_state["large_language_model"]

col1, col2 = st.columns([3, 1])

with col1:
    st.title(f"Simple Echo Bot")
    st.badge(str(model_status), color="red")

with col2:
    if st.button("Reset Chat history"):
        st.session_state.messages = []
        write_msg_history()

vector_store = st.session_state["qdrant_client"].get_vectorstore(st.session_state["email"], st.session_state["embedding_model"])

if "messages" not in st.session_state:
    st.session_state["messages"] = []

write_msg_history()

greet_msg = "How can I help you?" if len(st.session_state.messages) == 0 else "**On the line with context**" 

prompt = st.chat_input(greet_msg)

if prompt:
    st.session_state.messages.append({"role": "user", "context": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = st.write_stream(query_to_llm(prompt))

    st.session_state.messages.append({"role": "assistant", "context": response})