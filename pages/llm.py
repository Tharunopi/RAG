import streamlit as st

vector_store = st.session_state["qdrant_client"].get_vectorstore(st.session_state["email"], st.session_state["embedding_model"])
placeholder_1 = st.empty()

user_query = st.chat_input("How can we help you?")

if user_query:
    with st.chat_message("user", avatar="human"):
        st.write(user_query)