
import langchain
import os
print(f"Langchain file: {langchain.__file__}")
print(f"Langchain dir content: {os.listdir(os.path.dirname(langchain.__file__))}")
