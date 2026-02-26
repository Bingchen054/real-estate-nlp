import pandas as pd
import random
import os

os.makedirs("data/processed", exist_ok=True)

property_types = ["single family home", "condo", "townhouse", "duplex", "investment property"]
features = [
    "open floor plan", "hardwood floors", "granite countertops",
    "stainless steel appliances", "walk-in closet",
    "vaulted ceilings", "solar panels", "smart home system"
]
locations = [
    "near downtown", "close to schools", "minutes from shopping",
    "quiet neighborhood", "gated community",
    "near public transportation", "walking distance to parks"
]
conditions = [
    "move-in ready", "fully renovated", "needs TLC",
    "recently upgraded", "newly remodeled", "fixer upper"
]
amenities = [
    "community pool", "private backyard", "two-car garage",
    "large lot", "corner lot", "no HOA", "low HOA fees"
]

rows = []
num_rows = 1000

for i in range(num_rows):
    remark = f"""
    Beautiful {random.choice(property_types)} with {random.choice(features)}.
    Located {random.choice(locations)}.
    Property is {random.choice(conditions)} and includes {random.choice(amenities)}.
    Priced to sell with strong investment potential.
    """

    rows.append({
        "L_ListingID": 100000 + i,
        "L_Address": f"{100+i} Example St",
        "L_City": random.choice(["San Jose", "Los Angeles", "San Diego", "San Francisco"]),
        "beds": random.choice([1, 2, 3, 4, 5]),
        "baths": random.choice([1, 2, 3, 4]),
        "price": random.choice([350000, 450000, 550000, 650000, 750000, 850000, 950000]),
        "L_Remarks": remark.strip()
    })

df = pd.DataFrame(rows)
output_path = "data/processed/listing_sample.csv"
df.to_csv(output_path, index=False)

print("Sample dataset generated.")
print(f"Total records: {len(df)}")
print(f"Saved to: {output_path}")