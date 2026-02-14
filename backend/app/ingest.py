import os
import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB client
# stored in 'backend/chromedb' to persist data
CHROMA_DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chromedb")
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

# Use a default embedding function (Sentence Transformers)
# You might need to install: pip install sentence-transformers
default_ef = embedding_functions.DefaultEmbeddingFunction()

# Create or get the collection
collection = client.get_or_create_collection(
    name="pakistan_history",
    embedding_function=default_ef
)

def ingest_docs():
    """
    Reads text files from backend/data and ingests them into ChromaDB.
    """
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created data directory at {data_dir}. Please add .txt files there.")
        return

    files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
    
    if not files:
        print("No text files found in data directory.")
        return

    documents = []
    metadatas = []
    ids = []

    for filename in files:
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            documents.append(text)
            metadatas.append({"source": filename})
            ids.append(filename)

    if documents:
        collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Ingested {len(documents)} documents.")

def query_docs(query_text: str, n_results: int = 2):
    """
    Queries the collection for relevant documents.
    """
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results

if __name__ == "__main__":
    ingest_docs()