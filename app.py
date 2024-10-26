from flask import Flask, render_template, request, jsonify
from utils import tokenizer, tweet_sentiment_model, classes
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('tweet_sentiment.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['content']
    print(text)
    sequence = tokenizer.texts_to_sequences([text])
    print(sequence)
    sequence = pad_sequences(sequence, maxlen=25)
    prediction = tweet_sentiment_model.predict(np.array(sequence))
    pred_label = np.round(np.squeeze(prediction)).astype(int)
    pred_label = classes[pred_label]

    return jsonify({'prediction': pred_label})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)