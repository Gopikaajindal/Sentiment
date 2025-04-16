import pickle
from flask import Flask, request, jsonify
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer



app = Flask(__name__)

# === Load Model and Vectorizer ===
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# === MySQL Config ===
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",  # change if different
    "database": "imdb_reviews"
}

def connect_db():
    """Connect to MySQL"""
    return mysql.connector.connect(**db_config)

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()

        if not data or "review" not in data:
            return jsonify({"error": "Missing 'review' in JSON body"}), 400

        review_text = data["review"]

        # Vectorize and predict
        transformed_text = vectorizer.transform([review_text])
        prediction = model.predict(transformed_text)[0]

        # Map prediction
        label_map = {0: "negative", 1: "positive", 2: "neutral"}
        sentiment = label_map.get(prediction, "unknown")

        # Save result to DB
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reviews (review_text, sentiment) VALUES (%s, %s)",
            (review_text, sentiment)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            "review": review_text,
            "sentiment_prediction": sentiment
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
