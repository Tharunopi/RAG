import streamlit as st
from utils.document_structure import threadStructure
from utils.atlas import mongoClient
from uuid import UUID
from utils.lang_chain import chain
from utils.vector_search import searchVectorDB

if "search_vdb" not in st.session_state:
    st.session_state["search_vdb"] = searchVectorDB()
search_vdb = st.session_state["search_vdb"]

if "flow_chain" not in st.session_state:
    st.session_state["flow_chain"] = chain()
flow_chain = st.session_state["flow_chain"]

if "atlas_client" not in st.session_state:
    st.session_state["atlas_client"] = mongoClient()
atlas_client = st.session_state["atlas_client"]
atlas_client.init_db_and_collection()

def write_msg_history() -> None:
    """Render the chat history for the current thread in the app.
    Iterates over st.session_state.messages (list of dicts with 'role' and 'context')
    and displays each message using st.chat_message and st.markdown.
    Returns:
        None: This function renders UI elements and does not return a value.
    """
    for i in st.session_state.messages:
        with st.chat_message(i["role"]):
            st.markdown(i["context"])

def query_to_llm(prompt:str):
   """
    Stream the LLM response for a given prompt using the configured chain.
    Parameters:
        - prompt: Text to send to the chain as the 'question' variable.
    Returns:
        - Iterator[str]: Stream of response chunks produced by the LLM.
    """
   context = search_vdb.basic_search(prompt)
   return flow_chain.get_chain().stream({"context": context, "question": prompt})

def push_to_atlas(chat_message: dict) -> None:
    """
    Persist a chat message to Atlas for the current single-thread session.

    Builds a utils.document_structure.threadStructure from st.session_state["email"] and st.session_state["unique_single_thread_id"], then appends the provided message via utils.atlas.mongoClient.insert_document.

    Args:
        chat_message (dict): The message payload to persist.

    Returns:
        bool | None: True on success, False if the write produced no result, or None if an exception occurred.

    Side Effects:
        Reads st.session_state and prints a diagnostic message on failure.
    """
    try:
        details = threadStructure(email=st.session_state["email"], uuid=st.session_state["unique_single_thread_id"], message=chat_message)
        result = atlas_client.insert_document(details)
        if result is None: 
            return False
        return True

    except Exception as e:
        print(f"llm_helper.py -> push_to_atlas: {e}")

def delete_from_atlas(uuid: UUID):
    """
    Delete a document from Atlas by its UUID.

    Delegates to atlas_client.delete_document.

    Args:
        uuid (UUID): The unique identifier of the document to remove.

    Returns:
        bool: True if the document was deleted; otherwise False.
    """
    result = atlas_client.delete_document(uuid)
    return result

def retrieve_thread(email:str):
    result = atlas_client.get_thread(email)
    
    if not result:
        return []
    
    messages = result.get("message", [])

    if not isinstance(messages, list):
        messages = [messages]

    return messages