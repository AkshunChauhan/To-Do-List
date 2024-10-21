import os
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
def get_mongo_client():
    # MongoDB Atlas connection string from environment variable
    mongo_uri = os.getenv("MONGODB_URI")
    if mongo_uri is None:
        raise ValueError("The MongoDB connection string is not set in the environment variables.")
    return pymongo.MongoClient(mongo_uri)
