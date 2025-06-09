import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("digit_model.h5")

# Preprocess image function
def preprocess_image(image):
    image = image.convert("L")  # Grayscale
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    return img_array.reshape(1, 28, 28, 1)

# UI
st.set_page_config(page_title="Digit Recognizer", layout="centered")
st.title("🧠 Handwritten Digit Recognizer")
mode = st.radio("Choose input mode:", ["Upload Image", "Draw Digit"])

image = None

# Upload Option
if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload a digit image (0-9)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=False)

# Drawing Option
elif mode == "Draw Digit":
    # Create a unique key for the canvas based on a counter
    if 'canvas_key' not in st.session_state:
        st.session_state.canvas_key = 0

    canvas_result = st_canvas(
        fill_color="white",  # Background
        stroke_width=10,
        stroke_color="black",
        background_color="white",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key=f"canvas_{st.session_state.canvas_key}",
    )

    # Add clear canvas button
    if st.button("Clear Canvas"):
        st.session_state.canvas_key += 1
        st.experimental_rerun()

    if canvas_result.image_data is not None:
        image = Image.fromarray(np.uint8(canvas_result.image_data)).convert("RGB")
        st.image(image, caption="Drawn Image", width=150)

# Predict Button
if image and st.button("Predict"):
    processed = preprocess_image(image)
    pred = model.predict(processed)
    digit = np.argmax(pred)
    confidence = np.max(pred)
    
    st.success(f"Predicted Digit: {digit}")
    st.info(f"Confidence: {confidence:.2%}")
