import json
import pandas as pd
import re


TAXONOMY_PATH = "data/processed/taxonomy_structured.json"
DATA_PATH = "data/processed/listing_sample.csv"
QUERIES_PATH = "data/processed/user_queries.json"


def test_taxonomy_structure():
    with open(TAXONOMY_PATH) as f:
        data = json.load(f)

    total_terms = 0
    for category, terms in data["categories"].items():
        total_terms += len(terms)

    assert total_terms >= 200, "Taxonomy must contain at least 200 categorized terms."


def test_sample_data_quality():
    df = pd.read_csv(DATA_PATH)
    assert len(df) >= 500, "Sample dataset must contain at least 500 records."
    assert df["L_Remarks"].str.len().min() > 50, "All remarks must exceed 50 characters."


def test_user_queries():
    with open(QUERIES_PATH) as f:
        queries = json.load(f)

    assert len(queries) >= 50, "Must contain at least 50 user queries."
    assert all("intent" in q and "query" in q for q in queries), "Each query must have intent and query fields."


def test_taxonomy_coverage():
    with open(TAXONOMY_PATH) as f:
        taxonomy = json.load(f)

    df = pd.read_csv(DATA_PATH)

    terms = []
    for category in taxonomy["categories"].values():
        for item in category:
            terms.append(item["term"])

    pattern = re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b", re.IGNORECASE)

    matches = df["L_Remarks"].apply(lambda x: bool(pattern.search(str(x))))
    coverage = matches.mean()

    assert coverage >= 0.3, "Taxonomy coverage must be at least 30%."