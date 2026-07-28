import chromadb
from config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K_RESULTS,
)
from utils.embedding import EmbeddingModel

class QueryEngine:
    """
    Search the vector database for relevant document chunks.
    """

    def __init__(self) -> None:
        self.embedding_model = EmbeddingModel(EMBEDDING_MODEL)
        client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
        self.collection = client.get_collection(name=COLLECTION_NAME)

    def search(self, question: str) -> list[dict]:
        """
        Search the collection for the most relevant chunks.

        Args:
            question: User question.

        Returns:
            List of retrieved chunks with metadata.
        """

        question_embedding = self.embedding_model.encode([question])[0]

        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=TOP_K_RESULTS,
        )

        retrieved_chunks = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]
        ids = results["ids"][0]

        for document, metadata, distance, chunk_id in zip(
            documents,
            metadatas,
            distances,
            ids,
        ):
            retrieved_chunks.append(
                {
                    "id": chunk_id,
                    "content": document,
                    "source": metadata["source"],
                    "distance": distance,
                }
            )

        return retrieved_chunks