# DocuMind AI

AI-powered Document Intelligence + Agentic RAG system built for AI Engineer Internship Assessment.

## Live Demo

Frontend: https://docu-mind-jlwvd44ej-kanishkashukla04s-projects.vercel.app/

Backend API: https://documind-ai-production-8171.up.railway.app/

GitHub Repository: https://github.com/KanishkaShukla04/DocuMind-AI

## Overview

DocuMind AI processes real-world documents including PDFs, scanned documents, and image-based files.

The system:
- Extracts text from documents
- Generates page-level images
- Classifies documents using LLMs
- Creates searchable embeddings
- Uses RAG to answer questions with citations
- Supports document upload and multi-turn chat through FastAPI endpoints
- Persists vector data, metadata, and page images for later retrieval
- Exposes a Next.js frontend for upload and chat workflows

## Features

### Document Parser
- PDF text extraction
- PDF page rendering
- OCR support with Tesseract
- Stores extracted text and page images
- Extracts metadata for each uploaded document

### Document Classification

Each uploaded document is classified into:

- Document type
- Topic
- Sensitivity level
- Content characteristics
- Summary

Output is structured JSON.

### API Surface

- `POST /upload` for bulk document upload and indexing
- `POST /chat` for question answering with conversation history
- Upload responses include classification, document IDs, page counts, and processing status

### Agentic RAG Pipeline

The chatbot:

- Retrieves relevant document chunks
- Generates grounded answers
- Avoids hallucinations
- Provides source citations

Each answer includes:

- Document name
- Page number
- Page preview image
- Citation metadata for traceability

### Chat Interface

Supports:

- Multi-turn conversations
- Document-based questions
- Citation previews
- Chat history passed from the client to the backend

### Bulk Upload

Supports:

- Multiple document uploads
- Processing pipeline
- Knowledge base indexing
- Classification results shown per uploaded file

### Storage

- Uploaded files in `backend/uploads`
- Extracted metadata in `backend/metadata`
- Rendered page images in `backend/page_images`
- ChromaDB persistence in `backend/chroma_db`

## Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- Google Gemini API
- ChromaDB

### Frontend
- Next.js
- TypeScript
- Tailwind CSS

### Frontend App

- Next.js app router
- Upload page for document ingestion
- Chat page for querying indexed documents
- Shared API helpers in `frontend/lib`

### Document Processing

- pdfplumber
- pdf2image
- pytesseract

## Architecture

Upload

↓

Parser

↓

OCR

↓

Classifier

↓

Embedding

↓

Vector DB

↓

Retriever

↓

Gemini

↓

Answer + Citations

## Security Decisions

Implemented:
- Environment variables for secrets
- File isolation on the backend
- Separate upload and chat API routes
- No client-side API keys

Considered:
- Authentication
- Encryption at rest

Future:
- User-based document permissions

## Setup

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

## Project Notes

- Runtime artifacts live under `backend/chroma_db`, `backend/page_images`, `backend/metadata`, and `backend/uploads`.
- The app is designed to work with PDF and scanned document inputs.
- Classification data is returned alongside each uploaded document and can be rendered in the UI.