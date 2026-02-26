import pandas as pd

df = pd.read_csv("data/processed/listing_sample.csv")

with open("data/raw/mock_rets_property.sql", "a") as f:
    for _, row in df.iterrows():
        sql = f"""
INSERT INTO rets_property
(L_ListingID, L_Address, L_City, L_Keyword2, LM_Dec_3, L_SystemPrice, L_Remarks)
VALUES (
    {row['L_ListingID']},
    '{row['L_Address']}',
    '{row['L_City']}',
    {row['beds']},
    {row['baths']},
    {row['price']},
    "{row['L_Remarks'].replace('"', '')}"
);
"""
        f.write(sql)

print("SQL file generated successfully.")