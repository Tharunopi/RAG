import streamlit as st

email = st.session_state["email"]

try:
    pdfs = st.file_uploader(
        label="Upload PDF's",
        type="pdf",
        accept_multiple_files=True
    )  

    for i in pdfs:
        result = st.session_state["pdf_processor"].pdf_to_embeddings(i)
        with st.spinner(f"uploading embedding to {email}'s collection", show_time=True):
            push_status = st.session_state["qdrant_client"].upload_to_collection(email, result)

except Exception as e:
    print(e)