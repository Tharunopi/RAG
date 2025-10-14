from utils.qdrant_vector_db import qdrantDB
import streamlit as st

class searchVectorDB:
    def __init__(self):
        self.client = qdrantDB()

    def basic_search(self, query:str) -> list | None:
        try: 
            embedded_query = st.session_state["embedding_model"].embed_query(query)
            top_5 = self.client.similarity_search(st.session_state["email"], embedded_query)
            return [i.payload.get("page_content", "") for i in top_5]

        except Exception as e:
            print(f"searchVectorDB -> basic_search: {e}")