import pandas as pd
import re

# Load dataset
df = pd.read_csv("IMDB Dataset.csv")

# Function to clean text
def clean_text(text):
    text = str(text)  # Ensure it's a string
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text

# Apply cleaning function
df['review'] = df['review'].apply(clean_text)

# Save cleaned data
df.to_csv("IMDB_Cleaned_Dataset.csv", index=False)

print("Data cleaning complete! Cleaned data saved to IMDB_Cleaned_Dataset.csv")
  