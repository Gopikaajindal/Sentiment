import pandas as pd
import mysql.connector

# Load Dataset
df = pd.read_csv("IMDB_Cleaned_Dataset.csv")

# Connect to MySQL
conn = mysql.connector.connect(host="127.0.0.1", user="root", password="admin123", database="imdb_reviews")
cursor = conn.cursor()

cursor.execute("SHOW TABLES;")
for table in cursor.fetchall():
    print(table)

# Insert data
for _, row in df.iterrows():
    cursor.execute("INSERT INTO reviews (review_text, sentiment) VALUES (%s, %s)", (row['review'], row['sentiment']))

conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL!")
