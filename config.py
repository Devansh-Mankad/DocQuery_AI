from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
MODEL_DIR = BASE_DIR / "model"

# ChromaDB
COLLECTION_NAME = "college_documents"

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K_RESULTS = 3

# Gemma 4 E2B GGUF
LLM_MODEL_PATH = MODEL_DIR / "gemma4_E2B.gguf"

# Generation
MAX_TOKENS = 512
TEMPERATURE = 0.2
TOP_P = 0.9
TOP_K = 40
REPEAT_PENALTY = 1.1

# llama.cpp
N_CTX = 4096
N_THREADS = 4
N_BATCH = 256