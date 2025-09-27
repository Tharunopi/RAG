import os
from dotenv import load_dotenv
from supabase import Client, create_client
from utils.user_data import userData

schema_name = "public"
table_name = "user_data"

class supabaseClient():
    def __init__(self):
        load_dotenv()

        url: str = os.getenv("supabase_url")
        key: str = os.getenv("supabase_apikey")

        self.__supabase_client: Client = create_client(url, key)

    def fetch(self, table_name:str, select_statement:str="*"):
        """
        Runs select statement on given table, by default statement `*` and returns
        """
        response = self.__supabase_client.table(table_name) \
                    .select(select_statement) \
                    .execute()
        
        return response
    
    def upsert(self, data:userData):
        """
        Performs INSERT if data not present and UPDATE if data exists but different
        """
        response = self.__supabase_client.table(table_name) \
                        .upsert(data.get_data()) \
                        .execute()
        return response