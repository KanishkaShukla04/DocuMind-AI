# DocuMind AI

AI-powered Document Intelligence + Agentic RAG system built for AI Engineer Internship Assessment.

## Overview

DocuMind AI processes real-world documents including PDFs, scanned documents, and image-based files.

The system:
- Extracts text from documents
- Generates page-level images
- Classifies documents using LLMs
- Creates searchable embeddings
- Uses RAG to answer questions with citations

## Features

### Document Parser
- PDF text extraction
- PDF page rendering
- OCR support with Tesseract
- Stores extracted text and page images

### Document Classification

Each uploaded document is classified into:

- Document type
- Topic
- Sensitivity level
- Content characteristics
- Summary

Output is structured JSON.

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

### Chat Interface

Supports:

- Multi-turn conversations
- Document-based questions
- Citation previews

### Bulk Upload

Supports:

- Multiple document uploads
- Processing pipeline
- Knowledge base indexing

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

### Document Processing

- pdfplumber
- pdf2image
- pytesseract

## Architecture

User uploads document

↓

PDF Parser

↓

OCR/Text Extraction

↓

Document Classification

↓

Chunking + Embeddings

↓

Vector Database

↓

RAG Chatbot

↓

Answer + Citations

## Setup

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload