import streamlit as st

st.set_page_config(
    page_title="PDF chatbot",
    page_icon=r"C:\Stack overflow\RAG\src\trump_meme_icon.webp",
    layout="wide",
    initial_sidebar_state="auto"
)

if not st.user.is_logged_in:
    if st.button("login"):
        st.login()

