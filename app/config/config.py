import os

HF_TOKEN = os.environ.get("HF_TOKEN")

HUGGINGFACE_REPO_ID = "deepseek-ai/DeepSeek-R1"
DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

