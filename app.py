from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_reviews():
    reviews = request.json.get('reviews', [])
    print("Received reviews for analysis:", reviews)
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}

    for review in reviews:
        score = analyzer.polarity_scores(review)
        if score['compound'] >= 0.05:
            sentiments['positive'] += 1
        elif score['compound'] <= -0.05:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1

    print("Sentiment analysis result:", sentiments)
    return jsonify(sentiments)

if __name__ == '__main__':
    app.run(debug=True, port=5000)