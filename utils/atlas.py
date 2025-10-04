import pymongo, os
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from utils.document_structure import docStructure
from pymongo.results import InsertOneResult

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
            self.conn_status = False
        
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
            self.conn_status = True

        except Exception as e:
            print(f"mongoClient -> init_db_and_collection: {e}")

    def insert_document(self, document:docStructure) -> InsertOneResult | None:
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
        try:
            if not self.conn_status:
                self.init_db_and_collection()

            result = self.database.self.collection.insert_one(document)
            return result

        except Exception as e:
            print(f"mongoClient -> insert_document: {e}")
            return None
        
    def delete_document(self, document:docStructure) -> bool:
        """_summary_

        Args:
            document (docStructure): _description_

        Returns:
            bool: _description_
        """
        try: 
            pass
        
        except Exception as e:
            print(f"mongoClient -> delete_document: {e}")