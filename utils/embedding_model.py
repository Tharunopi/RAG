import os
from typing import Optional
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

class embeddingModel():
    def __init__(self):
        try:
            load_dotenv()
            self.__cohere_apikey: str = os.getenv("cohere_apikey")

        except Exception as e:
            print(f"From: __init__ - {e}")

    def get_embedding_model(self, model_name:str="embed-v4.0") -> Optional[CohereEmbeddings]:
        """
        Returns embedding model from huggingface default model
        """
        try:
            embeddings = CohereEmbeddings(
            cohere_api_key=self.__cohere_apikey,
            model=model_name
            )
            return embeddings

        except Exception as e:
            print(f"From: get_embedding_model - {e}")
            return None