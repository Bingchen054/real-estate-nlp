import json
import pandas as pd
import re

TAXONOMY_PATH = "data/processed/taxonomy_structured.json"
DATA_PATH = "data/processed/listing_sample.csv"

def load_terms():
    with open(TAXONOMY_PATH) as f:
        data = json.load(f)

    terms = []
    for category in data["categories"].values():
        for item in category:
            terms.append(item["term"])

    return terms

def calculate_coverage():

    df = pd.read_csv(DATA_PATH)
    terms = load_terms()

    pattern = re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b", re.IGNORECASE)

    matches = df["L_Remarks"].apply(lambda x: bool(pattern.search(str(x))))
    coverage = matches.mean()

    print("Total records:", len(df))
    print("Matched records:", matches.sum())
    print("Coverage:", round(coverage * 100, 2), "%")

if __name__ == "__main__":
    calculate_coverage()