import faiss, langchain_community, langchain_core
from langchain_community.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore

class vectorDataBase():
    def __init__(self):
        self.is_db_present = None

    def load_local_db(
            self, path:str, 
            emdeddings:langchain_core.embeddings.embeddings.Embeddings
            ) -> langchain_community.vectorstores.faiss.FAISS:
        try:
            vector_db = FAISS.load_local(path, embeddings=emdeddings, allow_dangerous_deserialization=True)
            self.is_db_present = True
            if self.is_db_present == True:
                print("Previous vector db is over written by this function")
            return vector_db

        except Exception as e:
            self.is_db_present = None
            print(f"Error: {e}")

    def initalize_empty_db(
            self, 
            emdeddingFunction:langchain_core.embeddings.embeddings.Embeddings, 
            index:str="hello world",
            indesToDocStoreID:dict={}
            ) -> langchain_community.vectorstores.faiss.FAISS:
        try:
            index = faiss.IndexFlatL2(len(emdeddingFunction.embed_query(index)))
            vector_db = FAISS(
                embedding_function=emdeddingFunction,
                index=index,
                docstore=InMemoryDocstore(),
                index_to_docstore_id=indesToDocStoreID
            )
            self.is_db_present = True
            if self.is_db_present == True:
                print("Previous vector db is over written by this function")
            return vector_db

        except Exception as e:
            self.is_db_present = None
            print(f"Error: {e}")