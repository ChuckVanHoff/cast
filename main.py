import pandas as pd

import config
import collect_owm
import load


# Specify the client to be used: either local or remote
client = config.client
# client = config.remote_client
# Check database access. If there is not remote access, then switch to local
 # instance of the database.
if load.check_db_access(client):
    # Set the database and collection and then collect and load data.
    db = config.database
    col = config.collection
    data = collect_owm.collect(limit=10)
    load_result = load.load(data, client, db, col)
    print(load_result)
else:
    print(f'The client you have specified, {client}, is not available.')
