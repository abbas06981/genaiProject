import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ✅ new imports
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval_qa.base import RetrievalQA

# load files
docs = []

loader = TextLoader("data/pakistan_history.txt")
docs.extend(loader.load())

# if pdf exists
# pdf_loader = PyPDFLoader("data/pakistan.pdf")
# docs.extend(pdf_loader.load())

# split text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = splitter.split_documents(docs)

# embeddings (Gemini)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# vector db
db = FAISS.from_documents(documents, embeddings)

# LLM Gemini
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

def ask_question(query):
    return qa.run(query)
