from pymongo import MongoClient

# Connection string to local MongoDB
MONGO_URL = "mongodb://localhost:27017"

# Create a MongoDB client
client = MongoClient(MONGO_URL)

# Choose (or create) a database
db = client["fullstack_app"]

# Access a collection (like a table in SQL)
messages_collection = db["messages"]
