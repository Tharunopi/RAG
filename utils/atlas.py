import pymongo, os
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class mongoClient():
    def __init__(self):
        """
        Init mongodb atlas client
        """
        try: 
            self.uri = os.getenv("mongodb_atlas_uri")
            self.client = MongoClient(self.uri, server_api=pymongo.server_api.ServerApi(version="1", strict=True, deprecation_errors=True))
            self.database = None
            self.collection = None
        
        except Exception as e:
            print(f"mongoClient -> __init__ : {e}")
    
    def check_connection(self) -> str | bool:
        """
        Checks the connection and returns timestamp, status string
        """
        try:
            self.client.admin.command("ping")
            return f"{datetime.now().strftime('%H:%M:%S')} --> Connected"
        
        except Exception as e:
            print(f"mongoClient -> check_connection: {e}")
            return False

    def init_db_and_collection(self, db:str="users", coll:str="users_chat_history_demo") -> None:
        """
        Init's database and collection
        """
        try:
            self.database = self.client[db]

            avail_collections = self.database.list_collection_names()
            if coll not in avail_collections:
                self.database.create_collection(coll)

            self.collection = self.database[coll]

        except Exception as e:
            print(f"mongoClient -> init_db_and_collection: {e}")

    def insert_document(self, document:dict) -> bool:
        """
        Insert document with the following structure,
        {
            email: str,
            chat_id: str,
            chat_name: str,
            messages: list[dict[str]],  
            metadata: dict
        }
        """