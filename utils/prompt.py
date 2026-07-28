def build_prompt(context: str, question: str) -> str:
    """
    Build the prompt sent to the language model.

    Args:
        context: Retrieved text from ChromaDB.
        question: User's question.

    Returns:
        Formatted prompt.
    """

    return f"""You are a helpful AI assistant for S.P.B Patel Engineering College.

Answer the user's question using only the provided context.

If the answer is not available in the context, reply:

"I couldn't find that information in the available documents."

Context:
{context}

Question:
{question}

Answer:"""