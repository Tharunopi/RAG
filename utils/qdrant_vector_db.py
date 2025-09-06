from dotenv import load_dotenv
import os
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_huggingface import HuggingFaceEndpointEmbeddings

try:
    load_dotenv()
    apikey = os.getenv("qdrant_apikey")
    url = os.getenv("qdrant_url")
    huggingface_apikey = os.getenv("huggingface_apikey")
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"

except Exception as e:
    print(e)

try:
    qdrant_client = QdrantClient(api_key=apikey, url=url)
    embeddings = HuggingFaceEndpointEmbeddings(
        huggingfacehub_api_token=huggingface_apikey
    )
except Exception as e:
    print(e)

def create_new_vector_db(email:str, dimension:int=768):
    """
    Creates a new collection returns True if success else False
    """
    try:
        qdrant_client.create_collection(
            collection_name=email,
            vectors_config=VectorParams(
                size=dimension,
                distance=Distance.COSINE
            )
        )
        return True

    except Exception as e:
        return False
        print(f"Error: {e}")

def get_collections():
    """
    Returns a list of existing collection name in list
    if error occurs then return None
    """
    try:
        collections = qdrant_client.get_collections().collections
        return [i.name for i in collections]
    except Exception as e:
        print(e)
        return None
    
def get_vectorstore(email:str):
    """
    Returns a vector collection based on collection name
    if error occurs then return None
    """
    try:
        db_store = QdrantVectorStore(
            client=qdrant_client,
            collection_name=email,
            embedding=embeddings
        )

    except Exception as e:
        print(e)
        return None

def get_embedding_model():
    """
    Returns the model used to embed documents or query
    if error occurs then return None
    """
    try:
        return embeddings

    except Exception as e:
        print(e)
        return None
    
def delete_collection(email:str):
    """
    Deletes collection using collection name
    if error occurs then return None
    """
    try:
        return qdrant_client.delete_collection(email)

    except Exception as e:
        print(e)
        return None