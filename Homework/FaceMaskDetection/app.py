import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('face_mask_detector_model.h5')

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = load_img(image, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Streamlit app
st.title("Face Mask Detection")
st.write("Upload an image to check if the person is wearing a mask or not.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Preprocess the image
    img_array = preprocess_image(uploaded_file)
    
    # Make prediction
    prediction = model.predict(img_array)
    if prediction[0][0] > 0.5:
        st.write("The person is **not** wearing a mask.")
    else:
        st.write("The person is wearing a mask.")
    
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
