import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.layers import GlobalMaxPooling2D


img_width, img_height = 80,60

print(tf.__version__)

def load_model():
    # Pre-Trained Model
    base_model = ResNet50(weights='imagenet', 
                        include_top=False, 
                        input_shape = (img_width, img_height, 3))
    base_model.trainable = False

    # Add Layer Embedding
    model = tf.keras.Sequential([
        base_model,
        GlobalMaxPooling2D()
    ])

    print(model.summary())
    return model

def get_embedding(model, img_path):
    # Reshape
    img = image.load_img(img_path, target_size=(img_width, img_height))
    # img to Array
    x   = image.img_to_array(img)
    # Expand Dim (1, w, h)
    x   = np.expand_dims(x, axis=0)
    # Pre process Input
    x   = preprocess_input(x)
    return model.predict(x,verbose=0).reshape(-1)