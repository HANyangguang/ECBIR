import glob
import pickle
import pandas as pd
from tqdm import tqdm
import nmslib

# For DELF loading
import tensorflow as tf
import tensorflow_hub as hub
from utils import *


def generate_dataset_vectors(paths):
    '''
    Call this method to generate feature vectors for each image in the dataset.
    '''
    tf.reset_default_graph()
    tf.logging.set_verbosity(tf.logging.FATAL)

    model = hub.Module('https://tfhub.dev/google/delf/1')

    image_placeholder = tf.placeholder(
        tf.float32, shape=(None, None, 3), name='input_image')

    module_inputs = {
        'image': image_placeholder,
        'score_threshold': 100.0,
        'image_scales': [0.25, 0.3536, 0.5, 0.7071, 1.0, 1.4142, 2.0],
        'max_feature_num': 1000,
    }

    module_outputs = model(module_inputs, as_dict=True)
    image_tf = paths_to_image_loader(list(paths))

    with tf.train.MonitoredSession() as sess:
        results_dict = {}
        for i in tqdm(range(len(paths))):
            image_path = paths[i]
            image = sess.run(image_tf)
            results_dict[image_path] = sess.run(
                [module_outputs['locations'], module_outputs['descriptors']], feed_dict={image_placeholder: image})
    return results_dict


paths = [img_path for img_path in sorted(
    glob.glob('static/dataset/*/*.[Jj][Pp][Gg]'))]
rea_dict = generate_dataset_vectors(paths)

paths = list(rea_dict.keys())
locations_agg = np.concatenate([rea_dict[img][0] for img in paths])
descriptors_agg = np.concatenate([rea_dict[img][1] for img in paths])
accumulated_indexes_boundaries = list(accumulate(
    [rea_dict[img][0].shape[0] for img in paths]))

# Space name
space_name = 'l2'
# Intitialize the library, specify the space, the type of the vector and add data points
index = nmslib.init(method='hnsw', space=space_name,
                    data_type=nmslib.DataType.DENSE_VECTOR)
index.addDataPointBatch(descriptors_agg)


# Set index parameters
# These are the most important onese
# Create an index
M = 15
efC = 100
num_threads = 4
index_time_params = {'M': M, 'indexThreadQty': num_threads,
                     'efConstruction': efC, 'post': 0}

index.createIndex(index_time_params)
index.saveIndex('static/feature/feature_set.bin')
pickle.dump(locations_agg, open('static/feature/locations_agg.pkl', 'wb'))
pickle.dump(accumulated_indexes_boundaries, open(
    'static/feature/accumulated_indexes_boundaries.pkl', 'wb'))
pickle.dump(paths, open('static/feature/paths.pkl', 'wb'))
