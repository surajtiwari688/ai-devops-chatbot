from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import ask_ai

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Welcome to AI ChatBot"}

@app.get("/health")
def health():
    return {
        "status": "UP",      
        "service": "AI ChatBot",}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = ask_ai(request.message)

    return {
        "user_message": request.message,
        "bot_reply": reply
    }