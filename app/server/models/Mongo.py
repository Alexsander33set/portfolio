import logging
import os
from typing import Any, Dict, Optional
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database

#* =====================================================

def _get_env_var(name: str) -> str:
    """Get environment variable or raise error if not set."""
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(
            f"Environment variable '{name}' is not set. "
            "Please check your .env file or environment configuration."
        )
    return value

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
    _client: Optional[MongoClient] = None
    _db: Optional[Database] = None
    _initialized: bool = False

    def __init__(self, collection_name: str):
        self._collection_name = collection_name
        self._collection = None

    @classmethod
    def _ensure_connection(cls):
        """Lazy initialization of MongoDB connection - only connects when first needed."""
        if cls._initialized:
            return

        mongo_url = _get_env_var("MONGO_URL")
        mongo_db_name = _get_env_var("MONGO_DB_NAME")

        cls._client = MongoClient(
            mongo_url,
            server_api=ServerApi('1'),
            serverSelectionTimeoutMS=5000,  # 5 second timeout for server selection
            connectTimeoutMS=5000,  # 5 second connection timeout
        )

        try:
            cls._client.admin.command('ping')
            logging.info("Successfully connected to MongoDB!")
        except Exception as e:
            logging.error("Failed to connect to MongoDB")
            logging.error(e)
            raise

        cls._db = cls._client[mongo_db_name]
        cls._initialized = True

    @property
    def client(self):
        MongoDB._ensure_connection()
        return MongoDB._client

    @property
    def db(self):
        MongoDB._ensure_connection()
        return MongoDB._db

    @property
    def collection(self):
        if self._collection is None:
            MongoDB._ensure_connection()
            self._collection = MongoDB._db[self._collection_name]
        return self._collection

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
