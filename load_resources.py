import streamlit as st
from utils.qdrant_vector_db import qdrantDB
from utils.embedding_model import embeddingModel
from utils.process_pdf import processPDF

def load():
    try:
        a, b, c = None, None, None
        if "qdrant_client" not in st.session_state:
            with st.spinner("Loading vector database...", show_time=True):
                st.session_state["qdrant_client"] = qdrantDB()
                a = True

        if "embedding_model" not in st.session_state:
            with st.spinner("Loading embedding model...", show_time=True):
                embedding_model = embeddingModel()
                st.session_state["embedding_model"] = embedding_model.get_embedding_model()
                b = True

        if "pdf_processor" not in st.session_state:
            with st.spinner("Loading PDF processor engine...", show_time=True):
                st.session_state["pdf_processor"] = processPDF(st.session_state["embedding_model"])
                c = True
        
        return (a, b, c)

    except Exception as e:
        print(f"load: {e}")
        return (None, None, None)
