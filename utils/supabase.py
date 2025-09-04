from dotenv import load_dotenv
from supabase import Client, create_client

class supabaseClient():
    def __init__(self):
        load_dotenv("../.env")

        url: str = ""
        key: str = ""

        self.__supabase_client = create_client(url, key)

    # def insert(self, )