
try:
    from langchain.chains import RetrievalQA
    print("Success: from langchain.chains import RetrievalQA")
except ImportError as e:
    print(f"Failed: from langchain.chains import RetrievalQA - {e}")

try:
    from langchain.chains.retrieval_qa.base import RetrievalQA
    print("Success: from langchain.chains.retrieval_qa.base import RetrievalQA")
except ImportError as e:
    print(f"Failed: from langchain.chains.retrieval_qa.base import RetrievalQA - {e}")
