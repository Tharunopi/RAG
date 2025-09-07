import streamlit as st
from load_resources import load

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
    load_result = load()
    db, emdedding_model, pdf_engine = st.session_state["loaded_qdrant_client"], st.session_state["loaded_embedding_model"], st.session_state["loaded_pdf_processor"]
    user_info = st.user.to_dict()
    st.session_state["email"] = user_info["email"]
    st.session_state["email_verified"] = user_info["email_verified"]
    st.session_state["name"] = user_info["name"]
    st.session_state["image"] = user_info["picture"]
    st.session_state["is_logged_in"] = user_info["is_logged_in"]

    db_result = st.session_state["qdrant_client"].create_new_vector_db(email=st.session_state["email"])
    
    col1, col2 = st.columns([1, 9])

    with col1:
        st.image("https://i.pinimg.com/736x/e8/56/3c/e8563cacce7c62309e4ff37756b796bc.jpg", width=150)

    with col2:
        if db is False:
            st.badge("Vector Database", color="red", icon=":material/close:")
        elif db:
            st.badge("Vector Database", color="green", icon=":material/check:")

        if emdedding_model is False:
            st.badge("Embedding Model", color="red", icon=":material/close:")
        elif db:
            st.badge("Embedding Model", color="green", icon=":material/check:")

        if pdf_engine is False:
            st.badge("PDF Engine", color="red", icon=":material/close:")
        elif db:
            st.badge("PDF Engine", color="green", icon=":material/check:")