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

        self.__supabase_client = create_client(url, key)

    def fetch(self, table_name:str, select_statement:str="*"):
        response = self.__supabase_client.table(table_name) \
                    .select(select_statement) \
                    .execute()
        
        return response
    
    def upsert(self, data:userData):
        if not self.check_if_exists():
            response = self.__supabase_client.table(table_name) \
                            .upsert(data.get_data()) \
                            .returning("minimal") \
                            .execute()
            return response