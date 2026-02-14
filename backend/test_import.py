try:
    import chromadb
    print(f"chromadb imported: {chromadb.__file__}")
    from chromadb.utils import embedding_functions
    print("embedding_functions imported successfully")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
