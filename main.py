import pandas as pd

import config
import collect_owm
import collect_wapi
import load


# Specify the client to be used: either local or remote
client = config.client
# client = config.remote_client
# Check database access. If there is not remote access, then switch to local
 # instance of the database.
if load.check_db_access(client):
    # Set the database and collection and then collect and load data.
    db = config.database_owm
    col = config.collection_owm
    data = collect_owm.collect(limit=10)
    load_result = load.load(data, client, db, col)
    print(load_result)
else:
    print(f'The client you have specified, {client}, is not available.')

if not load.check_db_access(client):
    import sys
    sys.exit()
# Now getting things ready for WeatherAPI data.
# Database:
db = config.database_wapi
col = config.collection_wapi
# Locations:
loc_list = []
with open('latlon_list.txt', 'r') as lst:
    for row in lst:
        loc_list.append(row)
data = collect_wapi.collect(loc_list[:10], days=2)
load_result = load.load(data, client, db, col)
print(load_result)
