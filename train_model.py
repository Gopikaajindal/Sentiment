import pandas as pd
import pickle
import mysql.connector
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# === MySQL Config ===
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"  # Update this if needed
MYSQL_HOST = "127.0.0.1"
DB_NAME = "imdb_reviews"
TABLE_NAME = "reviews"

# === Step 1: Create database if it doesn't exist ===
try:
    print("🔧 Connecting to MySQL to check/create database...")
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"✅ Database '{DB_NAME}' is ready.")
    cursor.close()
    conn.close()
except Exception as e:
    print("❌ Failed to connect to MySQL or create the database.")
    print(e)
    exit()

# === Step 2: Load data from table ===
try:
    print("📦 Connecting to the database and loading data...")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)

    # Load reviews table
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)
    print(f"✅ Loaded {len(df)} records from the '{TABLE_NAME}' table.")
except Exception as e:
    print("❌ Failed to load data. Make sure the 'reviews' table exists and has columns 'review_text' and 'sentiment'.")
    print(e)
    exit()

# === Step 3: Preprocessing ===
print("🧹 Cleaning and preparing data...")
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

X_train, X_test, y_train, y_test = train_test_split(
    df['review_text'], df['sentiment'], test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# === Step 4: Train Model ===
print("🧠 Training model...")
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# === Step 5: Evaluate ===
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.4f}")

# === Step 6: Save model and vectorizer ===
print("💾 Saving model and vectorizer...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("🎉 All done! Your model is trained and saved.")
