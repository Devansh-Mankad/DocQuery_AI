from config import CHUNK_OVERLAP, CHUNK_SIZE

def split_into_chunks(text: str) -> list[str]:
    """
    Split a document into overlapping text chunks.

    The document is first divided into paragraphs. Paragraphs are then
    combined until the configured chunk size is reached. Consecutive
    chunks share overlapping text to preserve context.
    """

    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 2 <= CHUNK_SIZE:
            if current_chunk:
                current_chunk += "\n\n"

            current_chunk += paragraph

        else:
            if current_chunk:
                chunks.append(current_chunk)

                overlap = current_chunk[-CHUNK_OVERLAP:]

                split_index = overlap.find("\n")

                if split_index != -1:
                    overlap = overlap[split_index + 1 :]

                current_chunk = overlap.strip()

                if current_chunk:
                    current_chunk += "\n\n"

            else:
                current_chunk = ""

            current_chunk += paragraph

    if current_chunk:
        chunks.append(current_chunk)

    return chunks