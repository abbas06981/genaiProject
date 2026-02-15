
try:
    print("Attempting to import rag...")
    import rag
    print("Successfully imported rag")
except Exception as e:
    print(f"Failed to import rag: {e}")
    import traceback
    traceback.print_exc()
