import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK resources
nltk.download('stopwords')

# Load pre-trained model and vectorizer C:\Users\Ravi\AI lab\Homework\vectorizer.pkl
with open("C:/Users/Ravi/AI lab/Homework/vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)
with open("C:/Users/Ravi/AI lab/Homework/model_LogisticRegression.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Preprocessing function
def preprocess_text(text):
    ps = PorterStemmer()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

# Streamlit UI
st.title("Fake News Detector")
user_input = st.text_area("Enter news text:")
if st.button("Predict"):
    processed_input = preprocess_text(user_input)
    vectorized_input = vectorizer.transform([processed_input]).toarray()
    prediction = model.predict(vectorized_input)[0]
    result = "Real News" if prediction == 1 else "Fake News"
    st.write(f"Prediction: {result}")
