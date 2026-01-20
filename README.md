🍅 AI Tomato Freshness Checker
A Full-Stack Computer Vision Application

The Problem: Manual inspection of produce is slow and subjective. The Solution: A Deep Learning system that classifies tomatoes into Fresh, Rotten, or Unripe with 96% accuracy.

🛠️ Tech Stack
Model: CNN built with TensorFlow/Keras.

API: FastAPI for high-performance model serving.

UI: Streamlit for a responsive user interface.

Processing: OpenCV for robust image normalization.

🚀 Key Features
Custom Data Pipeline: Built a custom Python generator to handle inconsistent image channels (RGB/RGBA/Grayscale).

Real-time Prediction: Sub-second inference time.

Mobile-Ready UI: Responsive design for field testing.



"Data Scarcity & Custom Curation" High-quality datasets for specific agricultural freshness stages are scarce. To solve this, I built a custom dataset of 320+ images across three distinct biological stages:

Fresh: Optimal peak ripeness, firm texture, uniform color.

Unripe: Pre-mature stage, characterized by high chlorophyll content (green/yellow hues).

Rotten: Post-consumer stage, showing fungal growth, bruising, and tissue degradation.
