from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_ai_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Study Assistant API running"}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_ai_response(request.message)
    return {"user": request.message, "reply": reply}