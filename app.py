import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cats_dogs_model.h5")

model = load_model()

IMG_SIZE = (128, 128)
class_names = ['Cat', 'Dog']  # change if needed

st.title("🐱🐶 Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it’s a cat or a dog.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and preprocess the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img = image.resize(IMG_SIZE)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    
    # If your model has 1 output neuron (sigmoid)
    if prediction.shape[1] == 1:
        label = "Dog" if prediction[0][0] > 0.5 else "Cat"
    else:  # if model outputs 2 neurons (softmax)
        pred_class = np.argmax(prediction[0])
        label = class_names[pred_class]

    st.write(f"### Prediction: {label}")
