from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
import PIL
import os
import io

from tensorflow.keras.models import load_model

my_dir = os.path.dirname(__file__)
h5_file_path = os.path.join(my_dir, 'flugVSkant.h5')
print(h5_file_path)

app = Flask(__name__)

@app.route("/")
def mainpage():

    return render_template("min_svamp_ai.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            # Read the uploaded image using PIL or any image processing library
            image_data = file.read()
            img = image.load_img(io.BytesIO(image_data), target_size=(160, 160))

            # Preprocess the image
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)

            model = load_model(h5_file_path)

            # Make a prediction
            prediction = model.predict(img)
            class_index = np.argmax(prediction)

            # Retrieve class labels or categories
            class_labels = ["Flug svamp", "Kantarell"]  # Replace with your own class labels

            print(prediction)
            result = {
                'class': class_labels[class_index],
                'confidence': str(prediction[0][class_index])
            }

            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
