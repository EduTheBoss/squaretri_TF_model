import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the  model
model_path = './models/triCuad.h5'
model = tf.keras.models.load_model(model_path)

def process_and_predict(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(256, 256))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Model expects a batch

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = 'triangle' if prediction > 0.5 else 'square'

    return image_path, predicted_class

if __name__ == "__main__":
    test_image_path = 'test.jpg'  
    result = process_and_predict(test_image_path)
    print("Image Path:", result[0], "Predicted Class:", result[1])
