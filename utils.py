import pickle
import tf_keras as tf
import tensorflow as tf

with open('models/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

tweet_sentiment_model = tf.keras.models.load_model(
    'models/tweet_sentiment_model.h5')

classes = ['Disaster', 'Suicide']
