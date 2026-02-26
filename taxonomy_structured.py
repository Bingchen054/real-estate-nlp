import json
import os

INPUT_PATH = "data/processed/taxonomy.json"
OUTPUT_PATH = "data/processed/taxonomy_structured.json"

CATEGORIES = {
    "Property_Type": [],
    "Property_Feature": [],
    "Property_Condition": [],
    "Location": [],
    "Financial": [],
    "Amenity": [],
    "Measurement": [],
    "Status_Legal": []
}

def categorize_term(term):
    """
    Basic rule-based categorization.
    This can later be replaced with ML-based classification.
    """

    property_types = ["condo", "townhouse", "duplex", "home", "property"]
    features = ["floor", "countertops", "appliances", "ceiling", "system"]
    conditions = ["renovated", "remodeled", "ready", "tlc", "upgraded"]
    location_words = ["downtown", "schools", "shopping", "neighborhood", "parks"]
    financial_words = ["priced", "investment", "sell", "value"]
    amenities = ["garage", "pool", "lot", "hoa", "backyard"]
    measurement_words = ["bedroom", "bathroom"]
    legal_words = ["hoa"]

    term_lower = term.lower()

    if any(word in term_lower for word in property_types):
        return "Property_Type"
    if any(word in term_lower for word in features):
        return "Property_Feature"
    if any(word in term_lower for word in conditions):
        return "Property_Condition"
    if any(word in term_lower for word in location_words):
        return "Location"
    if any(word in term_lower for word in financial_words):
        return "Financial"
    if any(word in term_lower for word in amenities):
        return "Amenity"
    if any(word in term_lower for word in measurement_words):
        return "Measurement"
    if any(word in term_lower for word in legal_words):
        return "Status_Legal"

    return None

def build_structured_taxonomy():

    with open(INPUT_PATH) as f:
        raw_taxonomy = json.load(f)

    for item in raw_taxonomy["terms"]:
        category = categorize_term(item["term"])
        if category:
            CATEGORIES[category].append(item)

    structured_taxonomy = {
        "meta": raw_taxonomy["meta"],
        "categories": CATEGORIES
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(structured_taxonomy, f, indent=2)

    print("Structured taxonomy created.")
    for category, items in CATEGORIES.items():
        print(f"{category}: {len(items)} terms")

if __name__ == "__main__":
    build_structured_taxonomy()