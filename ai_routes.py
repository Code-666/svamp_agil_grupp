from models import app
from flask import render_template, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import PIL
import io

model = load_model('flugVSkant.h5')

@app.route("/min_svamp_ai")
def min_svamp_ai():
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