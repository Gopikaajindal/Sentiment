import pandas as pd
import mysql.connector

# === Step 1: Load Dataset ===
df = pd.read_csv("IMDB_Cleaned_Dataset.csv")

# Rename column if needed (some CSVs use 'review' instead of 'review_text') 
if 'review' in df.columns and 'review_text' not in df.columns:
    df.rename(columns={'review': 'review_text'}, inplace=True)

# Check for required columns
if not {'review_text', 'sentiment'}.issubset(df.columns):
    print("❌ CSV must have columns: 'review_text' and 'sentiment'")
    exit()

# === Step 2: Connect to MySQL this is a very important step  ===
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",  # change if needed
    database="imdb_reviews"
)
cursor = conn.cursor()

# === Step 3: Create table if not exists ===
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        review_text TEXT,
        sentiment VARCHAR(10)
    )
""")

# === Step 4: Insert Data ===
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO reviews (review_text, sentiment) VALUES (%s, %s)",
        (row['review_text'], row['sentiment'])
    )

conn.commit()
cursor.close()
conn.close()

print("🎉 Data inserted into MySQL!")
