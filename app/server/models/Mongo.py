import os
from typing import Any, Dict
from pymongo import MongoClient
from pymongo.database import Database

#* =====================================================

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise AttributeError("MONGO_URL not defined")
MONGO_DB_NAME: str | Any = os.getenv("MONGO_DB_NAME")
if not MONGO_DB_NAME:
    raise AttributeError("MONGO_DB_NAME not defined")

#* project
#*
#* name
#* slug
#* description
#* technologies
#* url
#* priority
#* is_private
#* created_at
#*

    
class MongoDB:
    def __init__(self, collection_name: str):
        self.client: MongoClient[Dict[str, Any]] = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB_NAME]
        self.collection = self.db[collection_name]

    def insert_one(self, data):
        """Insere um documento na coleção"""
        result = self.collection.insert_one(data)
        return result.inserted_id

    def find_one(self, query):
        """Encontra um documento na coleção"""
        return self.collection.find_one(query)

    def find_all(self, query={}):
        """Encontra todos os documentos que correspondem ao critério de consulta"""
        return list(self.collection.find(query))

    def update_one(self, query, new_values):
        """Atualiza um documento na coleção"""
        return self.collection.update_one(query, {'$set': new_values})

    def delete_one(self, query):
        """Deleta um documento da coleção"""
        return self.collection.delete_one(query)
