import streamlit as st
from utils.llm_helper import write_msg_history, query_to_llm, push_to_atlas, delete_from_atlas, retrieve_thread
from uuid import uuid4

model_status = st.session_state["large_language_model_status"]
model = st.session_state["large_language_model"]

if "unique_single_thread_id" not in st.session_state:
    st.session_state.unique_single_thread_id = uuid4()

col1, col2 = st.columns([3, 1])

with col1:
    st.title(f"Simple Echo Bot")
    st.badge(str(model_status), color="red")

with col2:
    if st.button("Reset Chat history"):
        st.session_state.messages = []
        if not delete_from_atlas(st.session_state.unique_single_thread_id):
            st.error("Unable to delete thread chats")
    
        write_msg_history()

vector_store = st.session_state["qdrant_client"].get_vectorstore(st.session_state["email"], st.session_state["embedding_model"])

if "messages" not in st.session_state:
    value = retrieve_thread(st.session_state.email)
    st.session_state["messages"] = value

write_msg_history()

greet_msg = "How can I help you?" if len(st.session_state.messages) == 0 else "**On the line with context**" 

prompt = st.chat_input(greet_msg)

if prompt:
    user_msg = {"role": "user", "context": prompt}
    st.session_state.messages.append(user_msg)

    if not push_to_atlas(user_msg):
        st.error("Unable to update user chat to cloud")

    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = st.write_stream(query_to_llm(prompt))

    assistant_msg = {"role": "assistant", "context": response}
    st.session_state.messages.append(assistant_msg)

    if not push_to_atlas(assistant_msg):
        st.error("Unable to update assistant chat to cloud")