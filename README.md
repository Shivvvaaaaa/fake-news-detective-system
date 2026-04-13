# 📰 Fake News Detection System

## 📌 Overview

This project is a machine learning-based web application that detects whether a news article is **Fake** or **Real**.
It uses Natural Language Processing (NLP) techniques and a supervised learning model to classify news content.

---

## 🎯 Objective

* Identify fake news based on text patterns
* Apply machine learning for text classification
* Provide a simple web interface for users

---

## 📊 Dataset

* Dataset used: **WELFake Dataset**
* Contains labeled news articles:

  * `0` → Real News
  * `1` → Fake News

📥 Dataset Download:
👉 (PASTE YOUR GOOGLE DRIVE LINK HERE)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 🧠 Model Details

* Algorithm: **Logistic Regression**
* Feature Extraction: **TF-IDF Vectorizer**
* Type: **Supervised Learning (Text Classification)**

---

## 🔄 Workflow

```text
User Input
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Logistic Regression Model
   ↓
Prediction (Fake / Real)
```

---

## 🧹 Data Preprocessing

* Combined `title` and `text` columns
* Converted text to lowercase
* Removed special characters

---

## 📈 Results

* Achieved approximately **95% accuracy** on test data

---

## 🌐 Web Application

The model is deployed using Streamlit.

### Features:

* User input for news text
* Real-time prediction
* Confidence score display

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd FakeNewsProject
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run project.py
```

---

## ⚠️ Limitations

* The model does **not verify real-world facts**
* It detects fake news based on **text patterns**, not truth
* Performance may decrease for short or generic inputs

---

## 🔮 Future Improvements

* Integration with real-time fact-checking APIs
* Use of advanced models like BERT
* Improved dataset quality

-
