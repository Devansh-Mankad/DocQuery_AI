from pathlib import Path

def load_documents(data_dir: Path) -> list[dict]:
    """
    Load all text documents from the given directory.

    Returns:
        A list of dictionaries containing the document name and content.
    """

    documents = []

    for file_path in sorted(data_dir.glob("*.txt")):
        content = file_path.read_text(encoding="utf-8").strip()

        if not content:
            continue

        documents.append(
            {
                "filename": file_path.name,
                "content": content,
            }
        )

    return documents