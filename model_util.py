import tensorflow as tf
import cv2
import numpy as np

# Load model once at startup
MODEL = tf.keras.models.load_model('../models/tomato_model.keras')
CLASSES = ['Fresh', 'Rotten', 'Unripe']


def preprocess_image(image_bytes):
    # Convert bytes to opencv image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Standardize to RGB (The fix for your earlier crash!)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return np.expand_dims(img, axis=0)


def get_prediction(image_tensor):
    preds = MODEL.predict(image_tensor)
    idx = np.argmax(preds)
    return CLASSES[idx], float(preds[0][idx])