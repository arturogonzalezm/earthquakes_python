
# Earthquakes Python #
Extract the earthquakes from Geo JSON url using Python.

> ### Overview:
The purpose of this demo is to show how to return places and magnitude greater than 1.0 in a for loop.

> ### Technical Specs:
- IDE - PyCharm 2019.1
- Python 3.6.1
- Jupyter

> ### Instructions:

Import relevant libraries


```python
import requests
import numpy as np
```

Specify URL


```python
json_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
```

Send a request to the URL to retrieve data


```python
def load_json_data(earthquakes_url):
    data = requests.get(earthquakes_url).json()
    return data
```

Return list of places and magnitudes, where magnitude is greater than 1.0.
We have to convert the magnitude from str to float type and a very easy way is using Numpy data type.


```python
def read_url(data):
    earthquakes_data = load_json_data(data)
    for dictionary in earthquakes_data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        if np.array(magnitude, dtype=float) > 1.0:
            print(place, magnitude)
```

Call read_url()


```python
def main():
    read_url(json_url)
```

Execute


```python
if __name__ == '__main__':
    main()
```

----

MIT License

Copyright (c) 2019 Arturo Gonzalez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


```python

```
