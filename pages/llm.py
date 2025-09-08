import streamlit as st

vector_store = st.session_state["qdrant_client"].get_vectorstore(st.session_state["email"], st.session_state["embedding_model"])
text_query = st.text_input("Enter some text related to PDF's")

if st.button("Search"):
    query_result = vector_store.similarity_search(text_query)
    # document_id = [i._id for i in query_result]
    st.write(query_result)
    # st.write(document_id)