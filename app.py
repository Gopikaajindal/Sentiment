import pickle
from flask import Flask, request, jsonify
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load Model and Vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Database Connection
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "admin123",
    "database": "imdb_reviews"
}

def connect_db():
    """ Establish connection to MySQL database """
    return mysql.connector.connect(**db_config)

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    """ Predict sentiment using the trained model """
    try:
        data = request.get_json()
        if not data or "review" not in data:
            return jsonify({"error": "No review provided"}), 400

        review_text = data["review"]
        transformed_text = vectorizer.transform([review_text])
        prediction = model.predict(transformed_text)

        sentiment = "positive" if prediction[0] == 1 else "negative"

        # Save to database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reviews (review_text, sentiment) VALUES (%s, %s)", (review_text, sentiment))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"sentiment_prediction": sentiment})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
