import time
import requests
import numpy as np


def load_json_data(earthquakes_url):
    """
    :param earthquakes_url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    :return: Earthquakes json data
    """
    data = requests.get(earthquakes_url).json()
    return data


def read_url(data):
    """
    :param data: Earthquakes json data
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    earthquakes_data = load_json_data(data)
    for dictionary in earthquakes_data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        if np.array(magnitude, dtype=float) > 1.0:
            print(place, '|', magnitude)

    end = time.time()
    print('Time spent', end - start, 'seconds')
