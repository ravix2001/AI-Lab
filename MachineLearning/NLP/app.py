import streamlit as st
import joblib

# Load the trained model
model_path = "lr_model.gz"
@st.cache_resource
def load_model():
    return joblib.load(model_path)

# Predict category for a given input text
def predict_category(text):
    model = load_model()
    return model.predict([text])[0]

# Streamlit UI
st.title("Text Classification App")
st.write("Enter text below to predict its category using the trained Logistic Regression model.")

# User input
user_input = st.text_area("Enter text:")
if st.button("Predict"):
    if user_input:
        prediction = predict_category(user_input)
        st.success(f"Predicted Category: {prediction}")
    else:
        st.warning("Please enter some text to classify.")

st.write("Developed with ❤️ using Ravi")
