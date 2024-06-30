# For creating a list of coordinates.

import sys
import json

import coordinate_radius_v2 as cr2


def location_list(origin,
                  number=1,
                  radius=0,
                  ring=False,
                  disk=False,
                  geohash=False,
                  as_array=False
                 ):
    '''Make a list of at least one lat/lon geo coordiante centered at the given
    origin.
    :param origin: the location that all other locations will be wrt.
    :type origin: dict--lat/lon geocoordinates {'lat':[decnum],'lon':[decnum]}
    :param number: how many entries do you want in the list?
    :type number: int
    :param radius: the radius, in miles, of the coordinate ring
    :type radius: int
    
    '''
    
    # Check the type of the parameter and try to do something about it if it
    #  is not a dict.
    if not isinstance(origin, dict):
        print(f'''
        The given origin for the location_list function is not a dict.
        Its type is:
        {type(origin)}
        And this is what was given:
        {origin}
        ''')
        # Maybe it's a string-json...In the case that the given parameter
        #  is a string dict, try to get it into dict form.
        if not isinstance(origin, str):
            print('''
            The given variable "origin", in location_list(), is neither dict
            nor string...
            ''')
            sys.exit()
        try:
            origin = json.loads(origin)
            print(f'''tried to "json.loads()" origin, and I think it was 
            successful...
            origin = {origin}
            ''')
        except json.decoder.JSONDecodeError as jde:
            print('''
            I think you meant to write some code that would try to change
            single quotes into double quotes.
            ''')
        if isinstance(origin, dict):
            pass
        else:
            print('''
            From the function location_list(origin), origin is not a dict...
            exiting.
            ''')
            sys.exit()
    # Create a list of decimal lat-lon coordinates that map out to a ring of
    #  locations, centered about a given location or area.
    if ring == True:
        crg = cr2.CoordinateRadiusGenerator(origin['lat'], origin['lon'])
        coord_array = crg.get_coordinate_ring(radius, number)
        # This array needs to be returned as a list of dicts
        coord_list = []
        for row in coord_array:
            coords = {'lat': row[0], 'lon': row[1]}
            coord_list.append(coords)
        if as_array == True:
            return coord_array
        return coord_list
        
        
if __name__ == "__main__":
    origin = {'lat': 35.9289, 'lon': -62.0033}
    try:
        print(location_list(origin, number=10, radius=10, ring=True, as_array=True))
    except:
        print('there was an exception!')
        origin = {'lat': 35.9289, 'lon': -62.0033}
        location_list(origin, number=10, radius=10, ring=True)