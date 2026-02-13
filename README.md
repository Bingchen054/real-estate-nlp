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

### Backend / NLP
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Docker-4479A1?logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-Data_Processing-150458?logo=pandas&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-9C27B0)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5)
![Sentence-Transformers](https://img.shields.io/badge/Sentence--Transformers-Embeddings-FF6F00)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-009688)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn&logoColor=white)

### API / System
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![SQL](https://img.shields.io/badge/Parameterized-SQL-blue)
![Schema Validation](https://img.shields.io/badge/Schema-Validation-informational)

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
