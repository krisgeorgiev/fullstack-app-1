import os
from pymongo import MongoClient

# First look for env var MONGO_URL, otherwise default to localhost
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["fullstack_app"]
messages_collection = db["messages"]
