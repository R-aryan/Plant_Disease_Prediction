import numpy as np
import tensorflow as tf

# Keras
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# other utils
from src.config import Settings


class ModelPrediction:
    def __init__(self):
        # loading the settings
        self.target_size = Settings.TARGET_SIZE
        self.model_path = Settings.MODEL_PATH_INCEPTION

        # Load your trained model
        self.prediction_model = load_model(self.model_path)
        print(" Model Loaded Successfully....!!")

        self.predicted_text = " "

    def preprocess_image(self, image_path):
        print(image_path)
        img = image.load_img(image_path, target_size=self.target_size)

        # Preprocessing the image
        x = image.img_to_array(img)

        # Scaling

        x = x / 255
        x = np.expand_dims(x, axis=0)

        return x

    def model_predict(self, image_path):
        x = self.preprocess_image(image_path)
        prediction = self.prediction_model.predict(x)
        prediction = np.argmax(prediction, axis=1)

        if prediction == 0:
            self.predicted_text = "The leaf is diseased cotton leaf"
        elif prediction == 1:
            self.predicted_text = "The leaf is diseased cotton plant"
        elif prediction == 2:
            self.predicted_text = "The leaf is fresh cotton leaf"
        else:
            self.predicted_text = "The leaf is fresh cotton plant"

        return self.predicted_text
