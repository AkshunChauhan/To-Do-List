import os
import pymongo

def get_mongo_client():
    mongo_uri = os.getenv("MONGO_URL")
    return pymongo.MongoClient(mongo_uri)
