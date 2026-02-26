import pandas as pd
import nltk
from collections import Counter
from nltk.util import ngrams
import json
import os

nltk.download("punkt")

def build_taxonomy(
    input_path="data/processed/listing_sample.csv",
    output_path="data/processed/taxonomy.json",
    top_unigrams=300,
    top_bigrams=300,
    top_trigrams=200
):

    df = pd.read_csv(input_path)

    corpus = " ".join(df["L_Remarks"].astype(str).str.lower())

    tokens = nltk.word_tokenize(corpus)
    tokens = [t for t in tokens if t.isalpha()]

    unigram_freq = Counter(tokens).most_common(top_unigrams)
    bigram_freq = Counter(ngrams(tokens, 2)).most_common(top_bigrams)
    trigram_freq = Counter(ngrams(tokens, 3)).most_common(top_trigrams)

    terms = []
    term_id = 1

    for word, count in unigram_freq:
        terms.append({
            "id": term_id,
            "term": word,
            "ngram": 1,
            "frequency": count
        })
        term_id += 1

    for pair, count in bigram_freq:
        terms.append({
            "id": term_id,
            "term": " ".join(pair),
            "ngram": 2,
            "frequency": count
        })
        term_id += 1

    for triple, count in trigram_freq:
        terms.append({
            "id": term_id,
            "term": " ".join(triple),
            "ngram": 3,
            "frequency": count
        })
        term_id += 1

    taxonomy = {
        "meta": {
            "source_file": input_path,
            "total_terms": len(terms)
        },
        "terms": terms
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(taxonomy, f, indent=2)

    print("Taxonomy successfully built.")
    print(f"Total terms generated: {len(terms)}")
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    build_taxonomy()