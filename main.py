import streamlit as st
from utils.qdrant_vector_db import qdrantDB

st.set_page_config(
    page_title="PDF chatbot",
    page_icon=r"C:\Stack overflow\RAG\src\trump_meme_icon.webp",
    layout="wide",
    initial_sidebar_state="auto"
)

@st.cache_resource
def get_available_collections():
    db = qdrantDB()
    return db.get_collections()

@st.cache_resource
def cache_create_new_vector_db(email, *args, **kwargs):
    db = qdrantDB()
    return db.create_new_vector_db(email, *args, **kwargs)

@st.cache_resource
def cached_delete_collection(email):
    db = qdrantDB()
    return db.delete_collection(email)

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

    if "cleared_db" not in st.session_state:
        db_delete_result = cached_delete_collection(st.session_state["email"])

    db_result = cache_create_new_vector_db(email=st.session_state["email"])
    
    st.image("https://i.pinimg.com/736x/e8/56/3c/e8563cacce7c62309e4ff37756b796bc.jpg", width=150)
