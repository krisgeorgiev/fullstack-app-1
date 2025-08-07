from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allows frontend to talk to backend (via CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test route
@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

# POST route that the JS fetch() will call
@app.post("/message")
async def receive_message(request: Request):
    body = await request.json()
    message = body.get("message", "")

    print(f"[DEBUG] Received message: {message}")  # Optional: see in terminal

    return {"reply": f"Received: {message}"}
