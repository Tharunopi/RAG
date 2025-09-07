from dotenv import load_dotenv
import os
from typing import Optional
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_cohere import CohereEmbeddings

class qdrantDB():
    def __init__(self):
        try:
            load_dotenv()
            apikey = os.getenv("qdrant_apikey")
            url = os.getenv("qdrant_url")
            self.__qdrant_client = QdrantClient(api_key=apikey, url=url)

        except Exception as e:
            print(f"__init__: {e}")

    def create_new_vector_db(self, email:str, dimension:int=1536) -> bool:
        """
    Creates a new collection and returns it
    """
        try:
            self.__qdrant_client.recreate_collection(
                collection_name=email,
                vectors_config=VectorParams(
                    size=dimension,
                    distance=Distance.COSINE
                )
            )
            return True

        except Exception as e:
            print(f"create_new_vector_db: {e}")
            return False
    
    def get_collection_size(self, email:str) -> Optional[int]:
        """
        Returns a list of existing collection name in list
        """
        try:
            collection_size = self.__qdrant_client.get_collection(email)
            return collection_size.points_count
        except Exception as e:
            print(f"get_collections: {e}")
            return None

    def get_vectorstore(self, email:str, embeddings: CohereEmbeddings) -> Optional[QdrantVectorStore]:
        """
        Returns a vector collection based on collection name usually email
        """
        try:
            db_store = QdrantVectorStore(
                client=self.__qdrant_client,
                collection_name=email,
                embedding=embeddings
            )
            return db_store

        except Exception as e:
            print(f"get_vectorstore: {e}")
            return None
    
    def delete_collection(self, email:str):
        """
        Deletes collection using collection name returns true if success
        """
        try:
            return self.__qdrant_client.delete_collection(email)

        except Exception as e:
            print(f"delete_collection: {e}")
            return None

    def upload_to_collection(self,email:str ,embedded_values:list) -> Optional[bool]:
        """
        Upload embedded vectors to the existing collection
        """
        try:
            self.__qdrant_client.upload_collection(
                collection_name=email,
                vectors=embedded_values
            )
            return True

        except Exception as e:
            print(f"upload_to_collection: {e}")
            return None

    def similarity_search(self, email:str, query_vector:list, limit:int=5) -> Optional[list]:
        """
        Returns nearest neighbour
        """
        try:
            result = self.__qdrant_client.query_points(
                collection_name=email,
                query=query_vector,
                limit=limit
            )
            return result
        
        except Exception as e:
            print(f"similarity_search: {e}")