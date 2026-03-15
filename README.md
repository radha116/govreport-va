# GovReport-QA

A modern Retrieval-Augmented Generation (RAG) system that answers questions across multiple PDF reports using LangChain, FAISS, and the OpenAI API.

---

## Overview

GovReport-QA enables users to:

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
