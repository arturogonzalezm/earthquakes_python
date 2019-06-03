import time
import json
import numpy as np


def read_file(data):
    """
    :param data: Earthquakes json data
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    with open(data) as json_file:
        earthquakes_data = json.load(json_file)
    for dictionary in earthquakes_data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        if np.array(magnitude, dtype=float) > 1.0:
            print(place, '|', magnitude)

    end = time.time()
    print('Time spent', end - start, 'seconds')
