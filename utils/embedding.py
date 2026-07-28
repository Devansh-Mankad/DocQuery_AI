from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    """
    Wrapper around SentenceTransformer for generating text embeddings.
    """

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a list of text chunks.

        Args:
            texts: List of text chunks.

        Returns:
            List of embedding vectors.
        """

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings.tolist()