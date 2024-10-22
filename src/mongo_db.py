from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, log_entry):
        """Insert a log entry into the collection."""
        self.collection.insert_one(log_entry)

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()
