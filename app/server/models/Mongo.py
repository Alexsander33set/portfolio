import logging
import os
from typing import Any, Dict
from pymongo import MongoClient
from pymongo.server_api import ServerApi
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
#* status


class MongoDB:
    def __init__(self, collection_name: str):
        self.client: MongoClient[Dict[str, Any]] = MongoClient(MONGO_URL, server_api=ServerApi('1'))

        try:
            self.client.admin.command('ping')
            logging.info("Successfully connected to MongoDB!")
        except Exception as e:
            logging.error("Failed to connect at MongoDB")
            logging.error(e)

        self.db = self.client[MONGO_DB_NAME]
        self.collection = self.db[collection_name]

    def insert_one(self, data):
        """Insert a document into the collection"""
        result = self.collection.insert_one(data)
        return result.inserted_id

    def find_one(self, query):
        """Find a document into the collection"""
        return self.collection.find_one(query)

    def find_all(self, query=None):
        """Find all the documents that match the query criteria"""
        return list(self.collection.find(query))

    def update_one(self, query, new_values):
        """Updates a document in the collection"""
        return self.collection.update_one(query, {'$set': new_values})

    def delete_one(self, query):
        """Deletes a document from the collection"""
        return self.collection.delete_one(query)
