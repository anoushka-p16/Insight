from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    text = request.form['text_to_analyze']
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    return f'<h2>Sentiment: {sentiment}</h2><p>Polarity: {analysis.sentiment.polarity}</p>'

if __name__ == "__main__":
    app.run(debug=True)
