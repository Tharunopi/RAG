import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

class LLM():
    def __init__(
            self, 
            google_api_key:str=os.getenv("google_api_key"),
            include_thoughts:bool|None=None,
            temperature:float=0.7,
            verbose:bool=True
            ):
        self.google_api_key = google_api_key
        self.include_thoughts = include_thoughts
        self.temperature = temperature
        self.verbose = verbose

    def get_model(self, model_name:str="gemini-2.5-pro") -> GoogleGenerativeAI | None:
        """
        Returns the object of respective LLM
        """
        assert model_name in ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite"], "Plese Enter model with version above 2.5"

        try:
            llm = GoogleGenerativeAI(
                model=model_name,
                google_api_key=self.google_api_key,
                include_thoughts=self.include_thoughts,
                temperature=self.temperature,
                verbose=self.verbose
            )

            return llm
        except Exception as e:
            print(f"get_model: {e}")
            return None