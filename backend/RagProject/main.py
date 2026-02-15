from fastapi import FastAPI
from rag import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Pakistan History RAG API running"}

@app.get("/chat")
def chat(q: str):
    answer = ask_question(q)
    return {"question": q, "answer": answer}
