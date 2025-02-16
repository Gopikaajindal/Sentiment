# Sentiment Analysis Pipeline

## 📌 Project Overview

This project is a **Sentiment Analysis Pipeline** that processes textual data to determine sentiment polarity (positive, negative, or neutral). It uses Natural Language Processing (NLP) techniques and machine learning models to analyze the sentiment of given text data.

## 📂 Project Structure

```
📦 Sentiment-Analysis-Pipeline
├── app.py               # Main application file
├── data_cleaning.py     # Data preprocessing script
├── data_ingestion.py    # Data loading and processing script
├── model.py             # Model training and evaluation script
├── sentiment_analysis.iml  # Project configuration file
├── requirements.txt     # Python dependencies
├── sentiment_analysis.postman_collection.json  # API collection for testing
├── vectorizer.pkl       # Vectorizer file for text transformation
└── README.md            # Project documentation
```

## 🚀 Features

✅ Preprocesses textual data (removes noise, tokenization, lemmatization) ✅ Supports multiple machine learning models (Logistic Regression, Naive Bayes, etc.) ✅ Uses TF-IDF vectorization for feature extraction ✅ Provides a REST API for sentiment analysis ✅ Outputs sentiment as Positive, Negative, or Neutral

## 🛠 Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/manu0312/Sentiment-Analysis-Pipeline.git
   cd Sentiment-Analysis-Pipeline
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## 🔍 Usage

### **1️⃣ Data Preprocessing**

```sh
python data_cleaning.py
```

### **2️⃣ Train the Model**

```sh
python model.py
```

### **3️⃣ Run the API**

```sh
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

## 🎯 Example API Usage

Send a **POST** request to the API:

```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
```

Response:

```json
{
  "sentiment": "positive"
}
```

## 🛠 Technologies Used

- **Python** 🐍
- **Flask** (for API development)
- **Scikit-learn** (for machine learning models)
- **NLTK** (for text preprocessing)
- **Pandas & NumPy** (for data manipulation)


🚀 *Happy Coding!* 😊

