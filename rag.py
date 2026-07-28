from llama_cpp import Llama
from config import (
    LLM_MODEL_PATH,
    MAX_TOKENS,
    N_BATCH,
    N_CTX,
    N_THREADS,
    REPEAT_PENALTY,
    TEMPERATURE,
    TOP_K,
    TOP_P,
)

from query import QueryEngine
from utils.prompt import build_prompt

class RAGPipeline:
    """
    Retrieve relevant document chunks and generate an answer.
    """

    def __init__(self) -> None:
        self.query_engine = QueryEngine()

        self.llm = Llama(
            model_path=str(LLM_MODEL_PATH),
            n_ctx=N_CTX,
            n_threads=N_THREADS,
            n_batch=N_BATCH,
            verbose=False,
        )

    def ask(self, question: str) -> dict:
        """
        Generate an answer for the given question.

        Args:
            question: User question.

        Returns:
            Generated answer and retrieved sources.
        """

        retrieved_chunks = self.query_engine.search(question)

        context = "\n\n".join(chunk["content"] for chunk in retrieved_chunks)

        prompt = build_prompt(
            context=context,
            question=question,
        )

        response = self.llm(
            prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            top_k=TOP_K,
            repeat_penalty=REPEAT_PENALTY,
            echo=False,
        )

        answer = response["choices"][0]["text"].strip()
        seen: set[str] = set()
        sources: list[dict] = []
        for chunk in retrieved_chunks:
            name = chunk["source"]
            if name not in seen:
                seen.add(name)
                sources.append(
                    {
                        "source":  name,
                        "content": chunk["content"],
                        "score":   max(0.0, 1.0 - chunk.get("distance", 0.0)),
                    }
                )

        return {
            "answer":  answer,
            "sources": sorted(sources, key=lambda s: s["source"]),
        }