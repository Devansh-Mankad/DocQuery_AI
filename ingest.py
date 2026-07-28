import chromadb
from config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    DATA_DIR,
    EMBEDDING_MODEL,
)

from utils.loader import load_documents
from utils.chunker import split_into_chunks
from utils.embedding import EmbeddingModel

def main() -> None:
    documents = load_documents(DATA_DIR)
    embedding_model = EmbeddingModel(EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    chunk_count = 0

    for document in documents:
        chunks = split_into_chunks(document["content"])
        embeddings = embedding_model.encode(chunks)

        ids = []
        metadatas = []

        for index, chunk in enumerate(chunks):
            ids.append(f"{document['filename']}_{index}")

            metadatas.append(
                {
                    "source": document["filename"]
                }
            )

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        chunk_count += len(chunks)
    print(f"Indexed {chunk_count} chunks.")

if __name__ == "__main__":
    main()