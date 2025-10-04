import uuid
from uuid import UUID

class docStructure:
    def __init__(self, email:str, chat_name:str, messages:list[dict], metadata:dict, chat_id:UUID=uuid.uuid4(), summary:str|None=None):
        self.email = email
        self.chat_name = chat_name
        self.chat_id = chat_id
        self.messages = messages
        self.metadata = metadata
        self.entire_summary = summary

    def get(self):
        return {
            "_id": self.chat_id,
            "email": self.email,
            "chat_name": self.chat_name,
            "messages": self.messages,
            "metadata": self.metadata,
            "entire_summary": self.entire_summary
        }