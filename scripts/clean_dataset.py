import pandas as pd
from scripts.text_cleaning import TextCleaner

df = pd.read_csv("data/processed/listing_sample.csv")

cleaner = TextCleaner()

df["remarks_cleaned"] = df["L_Remarks"].apply(cleaner.clean_text)

df.to_csv("data/processed/listing_sample_cleaned.csv", index=False)

print("Cleaned dataset saved.")