# 🏠 Listing Intelligence System  
Real Estate NLP & Semantic Search Platform

A production-oriented NLP system that transforms unstructured MLS listing remarks into structured, searchable real estate intelligence.

This project simulates a real-world AI search system integrating data engineering, NLP pipelines, semantic retrieval, compliance detection, and API deployment.

---

## 🚀 Core Features

- MLS data ingestion from MySQL (Dockerized)
- Text cleaning & normalization (price, sqft, abbreviations)
- Named entity extraction (beds, baths, price, sqft)
- Natural language query → structured SQL filters
- Semantic search using Sentence Transformers + FAISS
- Listing summarization
- Fair Housing compliance detection
- REST API integration (FastAPI-ready)

---

## 🏗 System Flow

```
MySQL → Cleaning → Entity Extraction → Query Parsing
        → Semantic Search → Compliance Check → API
```

Designed with:

- Modular NLP architecture  
- Safe SQL generation (parameterized queries)  
- Schema validation  
- Production reliability  

---

## 📂 Project Structure

```
listing-intelligence-system/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_loading.py
│   ├── taxonomy_builder.py
│   └── text_cleaning.py
│
├── tests/
├── notebooks/
├── requirements.txt
└── docker-compose.yml
```

---

## 🚀 Tech Stack
## 🧱 Tech Stack

### Backend / NLP

* **Python 3.11+**
* **MySQL (Dockerized)**
* **pandas** for data processing
* **NLTK / spaCy** for text processing
* **Sentence-Transformers** for embeddings
* **FAISS** for vector similarity search
* **Scikit-learn** for classification & evaluation

### API / System

* **FastAPI** for RESTful service layer
* **Pytest** for unit testing
* **Docker** for containerized database setup
* Parameterized SQL for injection-safe query generation
* Schema validation for structured data integrity

### Architecture Highlights

* Modular NLP pipeline design
* Natural language → structured SQL parsing
* Embedding-based semantic search
* Compliance-aware text filtering

---

## ⚙️ Setup

```bash
git clone <repo-url>
cd listing-intelligence-system
docker-compose up -d

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

---

## 🎯 Highlights

- End-to-end NLP system (not just a model)
- Structured extraction from real-world MLS data
- Compliance-aware AI design
- Search + retrieval engineering
- Production-oriented architecture

---
