from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mongo.connection import messages_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for validation
class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

@app.post("/message")
async def receive_message(msg: Message):
    print(f"[DEBUG] Received message: {msg.message}")

    # Insert message into MongoDB
    messages_collection.insert_one({"message": msg.message})

    return {"reply": f"Stored: {msg.message}"}

@app.get("/test-mongo")
def test_mongo_connection():
    try:
        # List database names to check connection
        db_names = messages_collection.database.client.list_database_names()
        return {"status": "connected", "databases": db_names}
    except Exception as e:
        return {"status": "error", "details": str(e)}
 
from typing import List

@app.get("/messages")
def get_messages(limit: int = 10):
    """
    Return the latest messages from MongoDB.
    - limit: how many items to return (default 10)
    """
    # Exclude _id so you don't leak ObjectId into JSON
    cursor = messages_collection.find({}, {"_id": 0, "message": 1}).sort([("_id", -1)]).limit(limit)
    return {"items": list(cursor)}
