import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Tomato Freshness", layout="centered")
st.title("🍅 Tomato Freshness Checker")

uploaded_file = st.file_uploader("Upload tomato photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)

    # Create columns to center the image and keep it small
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Fixed width (e.g., 300px) prevents the massive height issue
        st.image(image, caption='Uploaded Tomato', width=300)

    if st.button("Check Freshness", use_container_width=True):
        with st.spinner('Analyzing...'):
            # Reset file pointer to beginning for the request
            files = {"file": uploaded_file.getvalue()}
            try:
                response = requests.post("http://127.0.0.1:8000/predict", files=files)
                result = response.json()

                # Big bold results
                st.subheader(f"Status: {result['status']}")
                st.progress(float(result['confidence'].replace('%', '')) / 100)
                st.write(f"Confidence: {result['confidence']}")
            except requests.exceptions.ConnectionError:
                st.error("Backend Not Found! Make sure uvicorn is running in Terminal 1.")