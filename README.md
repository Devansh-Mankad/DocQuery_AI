# DocQuery AI

A lightweight **Retrieval-Augmented Generation (RAG)** application built with Python, ChromaDB, Sentence Transformers, and a locally-running Gemma LLM.

Instead of relying on a model's internal knowledge, DocQuery retrieves the most relevant chunks from your own documents and uses them as grounded context for every answer.

---

## Features

- Local RAG pipeline — no external API calls
- Automatic document chunking and ingestion
- Semantic search via sentence embeddings
- ChromaDB vector store (persistent, local)
- Gemma GGUF inference via llama.cpp
- Streamlit web interface with source attribution

---

## Project Structure

```
DocQuery-AI/
│
├── app.py                  # Streamlit entry point
├── ingest.py               # Document ingestion pipeline
├── query.py                # Vector search engine
├── rag.py                  # RAG pipeline (retrieve + generate)
├── config.py               # Centralised configuration
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── components/
│   ├── chat.py
│   ├── footer.py
│   ├── header.py
│   ├── sidebar.py
│   └── source_panel.py
│
├── utils/
│   ├── chunker.py          # Text splitting
│   ├── embedding.py        # Embedding model wrapper
│   ├── loader.py           # Document loaders
│   └── prompt.py           # Prompt builder
│
├── data/                   # Source documents (not committed)
│   ├── handbook.txt
│   ├── library.txt
│   ├── hostel.txt
│   └── exam_rules.txt
│
├── chroma_db/              # Persisted vector database (not committed)
└── model/                  # GGUF model weights (not committed)
    └── gemma.gguf
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Interface | Streamlit |
| Vector Store | ChromaDB |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| LLM | Gemma 4 E2B (GGUF) |
| Inference | llama.cpp / llama-cpp-python |
| Language | Python 3.12 |

---

## How It Works

```
Your Documents
      │
      ▼
  Chunking          Split text into overlapping passages
      │
      ▼
  Embedding         Convert each chunk to a dense vector
      │
      ▼
  ChromaDB          Store and index all vectors locally
      │
  ┌───┴───┐
  │       │
  │  User Question
  │       │
  │       ▼
  │  Similarity Search   Find the top-K most relevant chunks
  │       │
  └──────►▼
  Retrieved Context
          │
          ▼
      Gemma LLM       Generate a grounded answer
          │
          ▼
        Answer  +  Sources
```

---

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Devansh-Mankad/DocQuery-AI.git
cd DocQuery-AI
```

**2. Create a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your documents**

Place `.txt`, `.pdf`, or other supported files in the `data/` directory.

**5. Download the model**

Download the Gemma GGUF weights and place the file at:

```
model/gemma.gguf
```

**6. Ingest documents**

```bash
python ingest.py
```

This chunks your documents, generates embeddings, and stores them in ChromaDB.

**7. Run the application**

```bash
streamlit run app.py
```

---

## Example Questions

**Attendance**
- What is the minimum attendance requirement?
- What documents are required for medical leave?

**Library**
- How many books can students borrow?
- What are the library timings?

**Hostel**
- When do hostel gates close?
- Are visitors allowed in the hostel?

**Examination**
- How are students graded?
- When are supplementary exams conducted?

---

## Configuration

All tuneable parameters live in `config.py`.

| Parameter | Default | Description |
|---|---|---|
| `CHUNK_SIZE` | `500` | Characters per chunk |
| `CHUNK_OVERLAP` | `100` | Overlap between chunks |
| `TOP_K_RESULTS` | `3` | Chunks retrieved per query |
| `MAX_TOKENS` | `512` | Max tokens in LLM response |
| `TEMPERATURE` | `0.2` | Generation temperature |
| `N_CTX` | `4096` | LLM context window |

---

## Learning Objectives

This project is a practical demonstration of:

- Retrieval-Augmented Generation (RAG) fundamentals
- How dense embeddings represent meaning
- Semantic similarity search vs keyword search
- ChromaDB as a local vector store
- Prompt engineering with retrieved context
- Running a quantised LLM entirely offline

---

## Author

**Devansh Mankad** — Computer Engineering Student

- GitHub: (https://github.com/Devansh-Mankad)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

If you found this useful, consider giving it a ⭐ on GitHub.