from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mongo.connection import messages_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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
 
