import pymongo
import streamlit as st

# MongoDB Configuration
def get_mongo_client():
    # MongoDB Atlas connection string from Streamlit secrets
    mongo_uri = st.secrets["mongodb"]["uri"]
    return pymongo.MongoClient(mongo_uri)
