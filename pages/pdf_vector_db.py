import streamlit as st
from utils.qdrant_vector_db import qdrantDB
from utils.embedding_model import embeddingModel
from utils.process_pdf import processPDF

try:
    with st.spinner("loading embedding model", show_time=True):
        embedding_client = embeddingModel()
        embedding = embedding_client.get_embedding_model()
    if embedding:
        st.success("Embedding model loaded successfully", icon="🔥")

    with st.spinner("loading vector db", show_time=True):
        vector_db_client = qdrantDB()
        vector_db = vector_db_client.get_vectorstore(email=st.session_state["email"], embeddings=embedding)
    if vector_db:
        st.success("Vector database loaded successfully", icon="🔥")

    with st.spinner("loading PDF miner", show_time=True):
        pdf_processor = processPDF(embedding)

except Exception as e:
    print(f"{e}")

try:
    pdfs = st.file_uploader(
        label="Upload PDF's",
        type="pdf",
        accept_multiple_files=True
    )  

    per_doc_embedding = []
    for i in pdfs:
        result = pdf_processor.pdf_to_embeddings(i)
        per_doc_embedding.append(result)

    
    

except Exception as e:
    print(e)