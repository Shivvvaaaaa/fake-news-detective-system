from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "5185e644a70f459d9cd8262bd2cf7b43"

@app.route("/predict", methods=["POST"])
def predict():
    news = request.json["news"]

    url = f"https://newsapi.org/v2/everything?q={news}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    total = data["totalResults"]

    if total > 5:
        result = "✅ Strongly verified news"
    elif total > 0:
        result = "⚠️ Possibly real (limited sources)"
    else:
        result = "❌ No trusted source found (suspicious)"

    return jsonify({"result": result})

app.run(debug=True)