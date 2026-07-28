# 📚 DocQuery-AI

A lightweight Retrieval-Augmented Generation (RAG) application built with **Python**, **ChromaDB**, **Sentence Transformers**, and a **local Gemma LLM**.

The application allows users to ask questions about local documents. Instead of relying on the LLM's internal knowledge, it retrieves the most relevant document chunks from a vector database and uses them as context to generate grounded answers.

---

## 🚀 Features

- Local Retrieval-Augmented Generation (RAG)
- Automatic document chunking
- Semantic search using embeddings
- ChromaDB vector database
- Local Gemma LLM integration
- Streamlit web interface
- Source-aware answers

---

## 🏗️ Project Structure

```
DocQuery-AI/

├── app.py
├── ingest.py
├── query.py
├── rag.py
├── config.py
├── requirements.txt
├── README.md

├── data/
│   ├── handbook.txt
│   ├── library.txt
│   ├── hostel.txt
│   └── exam_rules.txt

├── chroma_db/

├── models/
│   └── gemma.gguf

├── utils/
│   ├── chunker.py
│   ├── embedding.py
│   ├── loader.py
│   └── prompt.py
```

---

## ⚙️ Technologies

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- Gemma GGUF
- llama.cpp

---

## 🔄 Workflow

```
Documents
     │
     ▼
Chunking
     │
     ▼
Embedding Generation
     │
     ▼
ChromaDB
     ▲
     │
Question
     │
     ▼
Similarity Search
     │
     ▼
Retrieved Context
     │
     ▼
Gemma LLM
     │
     ▼
Answer
```

---

## 📚 Example Questions

### Attendance

- What is the minimum attendance requirement?
- Can I appear for exams with 70% attendance?
- What documents are required for medical leave?

### Library

- How many books can students borrow?
- What happens if I return books late?
- What are the library timings?

### Hostel

- When do hostel gates close?
- Are visitors allowed?
- What are hostel quiet hours?

### Examination

- How are students graded?
- Can I apply for revaluation?
- When are supplementary exams conducted?

---

## 🎯 Learning Objectives

This project demonstrates:

- What is RAG?
- What are embeddings?
- What is semantic search?
- How ChromaDB works
- Prompt engineering with retrieved context
- Local LLM integration

---

## ▶️ Run

Install dependencies

```bash
pip install -r requirements.txt
```

Ingest documents

```bash
python ingest.py
```

Run application

```bash
streamlit run app.py
```

---

# 👨‍💻 Author

**Devansh Mankad**

Computer Engineering Student

* GitHub: https://github.com/Devansh-Mankad
---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

---

# 📄 License

This project is licensed under the MIT License.