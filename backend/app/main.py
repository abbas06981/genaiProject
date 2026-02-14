from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

# Import the query function from ingest.py
# Make sure ingest.py is in the same directory (backend/app)
from app.ingest import query_docs

app = FastAPI()

# Allow CORS for the frontend
origins = [
    "http://localhost:3000",
    "http://localhost:3001",  # Add other ports if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Query the vector DB
        results = query_docs(request.question)
        
        # Extract the documents from the results
        # ChromaDB query result structure: {'ids': [...], 'distances': [...], 'metadatas': [...], 'documents': [...]}
        documents = results.get('documents', [[]])[0]
        
        if not documents:
            return {"answer": "I don't have enough information to answer that question based on the provided documents."}

        # Since we don't have an LLM connected yet, we return the most relevant document snippet
        # In a real RAG, we would pass 'documents' and 'request.question' to an LLM here.
        best_match = documents[0]
        
        return {"answer": f"Based on my knowledge: {best_match}..."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)