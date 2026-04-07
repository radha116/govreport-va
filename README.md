# GovReport-VA

A modern Retrieval-Augmented Generation (RAG) system that answers questions across multiple PDF reports using LangChain, FAISS, and the OpenAI API.

---

## Overview

GovReport-VA enables users to:

- Load multiple PDF documents
- Split them into text chunks
- Generate embeddings
- Store them in a FAISS vector database
- Ask natural language questions
- Receive answers grounded in the documents

This project demonstrates a full end-to-end RAG pipeline using the latest LangChain architecture (LCEL).

Example use case:
Analyzing archived strategic and performance reports from government sources.

---

## Features

- Multi-PDF document ingestion
- Text chunking with LangChain
- OpenAI embeddings
- FAISS vector similarity search
- Modern LangChain LCEL retrieval pipeline
- CLI-based question answering system
- Environment-based API key management
- Windows-compatible setup

---

## Tech Stack

- Python 3.10+
- LangChain (modern LCEL)
- langchain-community
- langchain-openai
- FAISS
- PyPDF
- python-dotenv
- OpenAI API

---

## Project Structure
![imagegithub](https://github.com/user-attachments/assets/0a0870a1-1c1b-4d4f-b38c-f1ee19d98f68)

---

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

### 3. Install Dependencies

pip install -r requirements.txt


---

### 4. Add OpenAI API Key

Create a `.env` file in the project root:
OPENAI_API_KEY=your_api_key_here


---

### 5. Add PDF Reports

Place your PDF files inside the `data/` folder.

Example sources:

https://department.va.gov/administrations-and-offices/management/archived-plans-and-reports/

---

### 6. Create Embeddings

Run:
python src\ingest.py

This will generate the `vector_db/` folder.

---

### 7. Run the Application
python src\app.py

Type your questions in the terminal.

To exit, type:

---

## Security Notes

This project excludes:

- Virtual environment (`venv/`)
- API keys (`.env`)
- Vector database files (`vector_db/`)
- Python cache files

Make sure your `.gitignore` includes:
venv/
.env
vector_db/
pycache/
