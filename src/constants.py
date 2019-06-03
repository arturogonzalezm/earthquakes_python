from datetime import date

json_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
path_us = '../data/'
file_name = "all_month-" + str(date.today().strftime('%d-%m-%Y')) + '.geojson'