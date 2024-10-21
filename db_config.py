import os
from dotenv import load_dotenv
import pymongo

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
def get_mongo_client():
    # MongoDB Atlas connection string from environment variable
    mongo_uri = os.getenv("MONGODB_URI")
    return pymongo.MongoClient(mongo_uri)
