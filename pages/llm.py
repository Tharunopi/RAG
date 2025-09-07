import streamlit as st

text_query = st.text_input("Enter some text related to PDF's")

if st.button("Search"):
    query_result = st.session_state["qdrant_client"].similarity_search(
        st.session_state["email"],
        st.session_state["embedding_model"].embed_query(text_query)
    )
    st.write(query_result)