# Code related to the colleciton of data through the OpenWeatherMaps API
import json
import requests
import pandas as pd
import keys


def collect(limit=10):
    # first get the locations established
    test_key = keys.test # The OWM api key that I use for testing
    loc_list = [] # An empty list to hold the lat-lon locations.
    uri_list = []
    data_list = []

    with open('latlon_list.txt', 'r') as lst:
        for row in lst:
            loc_list.append(row)
    # Create the uri's for pd.json_normalize() to work with.
    for coords in loc_list[:limit]:
        coord = json.loads(coords)
        lat = coord['lat']
        lon = coord['lon']
        uri = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={test_key}'
        uri_list.append(uri)
    # now make the requests
    for uri in uri_list:
        data = requests.get(uri).json()
        data = pd.json_normalize(data)
        data_list.append(data)
    return data_list


if __name__ == "__main__":
    print(collect())
