# Code to assist with loading  collected data to a MongoDB database.

# first verify the database:
#  -check for a server, either remote or local
#  -check for write access
# load the data to the database


import config

host = config.host
port = config.port
uri = config.uri

def check_db_access(client):
    ''' A check that there is write access to the database. '''

    db = client.test_db
    col = db.test_col
    db_count_pre = 0
    db_count_poost = 0
    
    # Check on this particular client's write status.
    try:
        if client.admin.command('ismaster'):
            print('You have write access!')
        else:
            print('According to the docs, this command came from a secondary \
            member or an arbiter of a replica set. You have no write access.')
    except ConnectionFailure:
        print("Server not available")
        return False
    return True

def load(data, client):
    ''' Load data to the specified MongoDB database.
    Data can be either a list of dicts or a single dict.'''
    temp = []
    if check_db_access(client):
        db = client.config.database
        col = db.config.collection
    if isinstance(data, list):
        # This is just to be sure that the correct load function is used:
         # insert one or insert many.
        for row in data:
            temp.append(row)
        insert_many_result = col.insert_many(temp)
        return insert_many_result
    else:
        insert_one_result = col.insert_one(data)
        return insert_one_result
        
