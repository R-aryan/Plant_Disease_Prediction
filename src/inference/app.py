# from __future__ import division, print_function
import sys
import os
import glob
import re

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# prediction utils
from src.inference.predict import ModelPrediction

# Define a flask app
app = Flask(__name__)

# create model prediction instance
model = ModelPrediction()


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        base_path = os.path.dirname(__file__)

        file_path = os.path.join(
            base_path, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # make prediction
        prediction = model.model_predict(file_path)

        return prediction
