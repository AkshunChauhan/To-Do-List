import os
import pymongo

# MongoDB Configuration
def get_mongo_client():
    # MongoDB Atlas connection string from environment variable
    mongo_uri = os.getenv("mongodb+srv://akshunchauhan099:FegZInm6MXJmc4hi@cluster0.b0kvq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    return pymongo.MongoClient(mongo_uri)
