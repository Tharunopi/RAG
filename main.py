import streamlit as st
from utils.qdrant_vector_db import create_new_vector_db, get_collections, get_vectorstore

st.set_page_config(
    page_title="PDF chatbot",
    page_icon=r"C:\Stack overflow\RAG\src\trump_meme_icon.webp",
    layout="wide",
    initial_sidebar_state="auto"
)


if not st.user.is_logged_in:
    if st.button("login"):
        st.login()

if st.user.is_logged_in:
    user_info = st.user.to_dict()
    st.session_state["email"] = user_info["email"]
    st.session_state["email_verified"] = user_info["email_verified"]
    st.session_state["name"] = user_info["name"]
    st.session_state["image"] = user_info["picture"]
    st.session_state["is_logged_in"] = user_info["is_logged_in"]

    available_collections = get_collections()
    if st.session_state["email"] not in available_collections:
        db_result = create_new_vector_db(email=st.session_state["email"])
    
    st.image("https://i.pinimg.com/736x/e8/56/3c/e8563cacce7c62309e4ff37756b796bc.jpg", width=150)
