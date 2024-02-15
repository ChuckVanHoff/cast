# Code related to the colleciton of data through the OpenWeatherMaps API
# I think this is intended to be used by an import and then reference 
# using a "[].collect()" command in code somewhere else.
import json
import requests
import pandas as pd

import keys


def collect(limit=10):
    # Request from OWM and return a single or a list of responses as DataFrames
    #  First get the locations established
    test_key = keys.test # The OWM api key that I use for testing
    loc_list = [] # An empty list to hold the lat-lon locations.
    uri_list = [] # An empty list to hold the uri's to be requested.
    data_list = [] # An empty list to hold the requested data.

    with open('latlon_list.txt', 'r') as lst:
        for row in lst:
            loc_list.append(row)
    #  Create the uri's to be used for the requests.
    for coords in loc_list[:limit]:
        coord = json.loads(coords)
        lat = coord['lat']
        lon = coord['lon']
        uri_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={test_key}'
        uri_forecast = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={test_key}'
        uri_list.append(uri_weather)
        uri_list.append(uri_forecast)
    #  Now make the requests
    print('requesting data...')
    for uri in uri_list:
        data_weather = requests.get(uri_weather).json()
        data_forecast = requests.get(uri_forecast).json()
        data_list.append(data_weather)
        data_list.append(data_forecast)
    return data_list


if __name__ == "__main__":
    print(collect())
