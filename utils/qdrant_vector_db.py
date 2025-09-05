from dotenv import load_dotenv
import os
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
apikey = os.getenv("qdrant_apikey")
url = os.getenv("qdrant_url")

qdrant_client = QdrantClient(api_key=apikey, url=url)
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/gemini-embedding-001",
#     task_type="retrieval_document"
# )

def create_new_vector_db(email:str, dimension:int=1536):
    try:
        qdrant_client.recreate_collection(
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
    try:
        collections = qdrant_client.get_collections().collections
        return [i.name for i in collections]
    except Exception as e:
        return e
    
def get_existing_collections(email:str):
    pass