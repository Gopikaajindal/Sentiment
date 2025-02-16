import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sqlalchemy import create_engine

# Load Data from MySQL
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1", user="root", password="admin123", database="imdb_reviews")


# Define MySQL connection URL
DATABASE_URL = "mysql+pymysql://root:admin123@localhost/imdb_reviews"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Read data using SQLAlchemy
df = pd.read_sql("SELECT * FROM reviews", engine)
conn.close()

# Convert labels
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# Split Data
X_train, X_test, y_train, y_test = train_test_split(df['review_text'], df['sentiment'], test_size=0.2, random_state=42)

# Feature Extraction
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Save Model & Vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
print("Model saved!")
