import os
import cv2
import json
import time
import pickle
import werkzeug
import pandas as pd
import nmslib

#For DELF loading
import tensorflow as tf
import tensorflow_hub as hub

from PIL import Image, ImageOps
from utils import find_close_books

#import Flask dependencies
from flask import Flask, request, render_template, jsonify, send_from_directory

#Set root dir
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

with open("static/feature/locations_agg.pkl", 'rb') as f:
	locations_agg = pickle.load(f)
with open("static/feature/accumulated_indexes_boundaries.pkl", 'rb') as f:
	accumulated_indexes_boundaries = pickle.load(f)
with open("static/feature/paths.pkl", 'rb') as f:
	paths = pickle.load(f)

space_name='l2'
# Re-intitialize the library, specify the space, the type of the vector.
newIndex = nmslib.init(method='hnsw', space=space_name, data_type=nmslib.DataType.DENSE_VECTOR)
# For an optimized L2 index, there's no need to re-load data points, but this would be required for
# non-optimized index or any other methods different from HNSW (other methods can save only meta indices)
#newIndex.addDataPointBatch(data_matrix)

# Re-load the index and re-run queries
newIndex.loadIndex('static/feature/feature_set.bin')

# Setting query-time parameters and querying
efS = 100
query_time_params = {'efSearch': efS}
print('Setting query-time parameters', query_time_params)
newIndex.setQueryTimeParams(query_time_params)


#Define Flask app
app = Flask(__name__)

#Define apps home page
@app.route("/", methods=['GET', 'POST']) 
def index():
    if request.method == 'POST':
        upload_dir = os.path.join(APP_ROOT, "static/uploads/")
        if not os.path.isdir(upload_dir):
            os.mkdir(upload_dir)
        resized_dir = os.path.join(APP_ROOT, "static/resized/")
        if not os.path.isdir(resized_dir):
            os.mkdir(resized_dir)
        imagefile = request.files['query_img']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(upload_dir + filename)
        #Perform the inference process on the uploaded image
        results = find_close_books(upload_dir + filename, resized_dir + filename, locations_agg, accumulated_indexes_boundaries, newIndex,)
        book_covers = [(paths[result[0]], result[1]) for result in results]
        return render_template('index.html', query_path = 'static/uploads/' + filename, cover_results = book_covers)
    else:
        return render_template("index.html")

#Start the application
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
