from utils.vector_search import searchVectorDB
import streamlit as st

vector = searchVectorDB()

result = vector.basic_search("What is langchain?")
print(result)