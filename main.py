import streamlit as st
from utils.qdrant_vector_db import create_new_vector_db, get_collections

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


    db_result = create_new_vector_db(email=st.session_state["email"])
    st.write(db_result)
    st.write(get_collections())
    st.image("https://www.memecreator.org/static/images/memes/3796301.jpg")
