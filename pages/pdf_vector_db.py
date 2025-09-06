import streamlit as st
from utils.qdrant_vector_db import get_vectorstore, get_embedding_model

try:
    vector_db = get_vectorstore(email=st.session_state["email"])
    embedding = get_embedding_model()

except Exception as e:
    print(f"{e}")

try:
    pdfs = st.file_uploader(
        label="Upload PDF's",
        type="pdf",
        accept_multiple_files=True
    )  

    st.write(pdfs)

except Exception as e:
    print(e)