import streamlit as st

st.title("Simple Echo Bot")

vector_store = st.session_state["qdrant_client"].get_vectorstore(st.session_state["email"], st.session_state["embedding_model"])

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for i in st.session_state["messages"]:
    with st.chat_message(i["role"]):
        st.markdown(i["content"])
    
if prompt := st.chat_input("what is up?"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Mirror: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})