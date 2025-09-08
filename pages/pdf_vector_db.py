import streamlit as st
import pandas as pd

email = st.session_state["email"]
placeholder_1 = st.empty()
placeholder_2 = st.empty()

try:
    pdfs = st.file_uploader(
        label="Upload PDF's",
        type="pdf",
        accept_multiple_files=True
    )  

    for i in pdfs:
        if i.name not in st.session_state["processed_pdf_name"]["file_name"]:
            result, page_content = st.session_state["pdf_processor"].pdf_to_embeddings(i)
            with st.spinner(f"uploading embedding to {email}'s collection", show_time=True):
                push_status = st.session_state["qdrant_client"].upload_to_collection(email, result, page_content)
            length_vector = st.session_state["qdrant_client"].get_collection_size(email)
            st.session_state["processed_pdf_name"]["file_name"].append(i.name)
            st.session_state["processed_pdf_name"]["chunk_sizes"].append(length_vector)
            
        else:
            st.toast(f"{i.name} is already processed", icon="🚨")

        with placeholder_2:
            collection_size = st.session_state["qdrant_client"].get_collection_size(email)
            if collection_size is None:
                st.badge("Failed to fetech DB size", color="red")
            else:
                st.badge(f"DB size: {collection_size}", color="green")

        with placeholder_1:
            df = pd.DataFrame(st.session_state["processed_pdf_name"])
            st.dataframe(df, width="content", hide_index=True)
        
except Exception as e:
    print(e)