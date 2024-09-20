from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    # Remplacez ceci par votre logique d'interaction avec l'API Groq
    return {"response": f"You asked: {request.prompt}"}
