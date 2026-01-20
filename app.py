from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
import cv2
import uvicorn

app = FastAPI()

# Load the brain you just trained
model = tf.keras.models.load_model('tomato_freshness_model.keras')
class_names = ['Fresh', 'Rotten', 'Unripe']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # The "Unbreakable" Preprocessing
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    predictions = model.predict(img)
    label = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return {"status": label, "confidence": f"{confidence*100:.2f}%"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)