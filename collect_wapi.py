# Script to request from source.

import json
import requests
import pprint

import keys

# build url for weatherapi
key = keys.weatherapi_test
base = 'http://api.weatherapi.com/v1'
forecast = '/forecast.json'
days = f'&days={1}'

def collect(locations, base=base, key=key, forecast=forecast, days=days):
    '''For the extraction of data from WeatherAPI.com.
    :param locations: the location to be requested
    :type locations: a list of dicts or jsons in the form {'lat':33, 'lon':75}
    :param base: the url base string
    :type base: string
    :param key: the api key required for the data request
    :type key: string
    :param forecast: this just tells the api which data set is being requested
    :type forecast: string--"forecast" 
                            It could also be "current" to have only current
                            weahter information returned.
    :param days: the number of days requeted in the forecast.
    :type days: string
    '''
    
    data = [] # The is to be filled and returned.
    print('requesting data...')
    for loc in locations: # Verify the data types and cast when needed.
        if not isinstance(loc, dict):
            if isinstance(loc, str):
                loc = json.loads(loc)
            else:
                print(f'''from collect_wapi.collect(), locations have to be
                type dict of type string, but it is {type(loc)}.''')
        # For getting the current weather for the "current" variable. Otherwise
         # use the forecast variable and specify the number of days of forcast
         # to be returned. **Note that forecast also returns current weather.**
        url_forecast = f'{base}{forecast}?key={key}&q={int(loc["lat"])},{int(loc["lon"])}{days}'
        # Request the data from the url.
        data.append(requests.get(url_forecast).json())
    return data


if __name__ == '__main__':
    # This should have the list of locations on which weahter data will be
    #  requested.
    locations = [{'lat': 75,
                 'lon': -75
                 },
                 {'lat': 59,
                 'lon': 5
                 }
                ]
    data = collect(locations)
    print(pprint.pprint(data))
    