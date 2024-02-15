# Code to assist with loading  collected data to a MongoDB database.

# first verify the database:
#  -check for a server, either remote or local
#  -check for write access
# load the data to the database


from pymongo.errors import ServerSelectionTimeoutError

import config


def check_db_access(client):
    ''' A check that there is write access to the database. '''
    
    # Check on this particular client's write status.
    try:
        if client.admin.command('ismaster'):
            print('You have write access!')
        else:
            print('According to the docs, this command came from a secondary \
            member or an arbiter of a replica set. You have no write access.')
    except ServerSelectionTimeoutError as e:
        print("ServerSelectionTimeoutError--Server not available")
        return False
    except ConnectionFailure:
        print("ConnectionFailure--Server not available")
        return False
    return True

def load(data, client, database, collection):
    ''' Load data to the specified MongoDB database.
    Data can be either a list of dicts or a single dict.
    
    :param data: the data to be loaded
    :type data: must be dict-like or a list of dict-like
    :param client: The database client
    :type client: MongoClient
    :param database: the database name
    :type database: string
    :param clooection: the collection name
    :type collection: string
    '''

    
    db = client[database]
    col = db[collection]
    temp = []
    print('loading data...')
    if isinstance(data, list): # This is just to be sure that the correct
                                # load function is used: load one or many.
        for row in data:
            temp.append(row)
        insert_many_result = col.insert_many(temp)
        return insert_many_result
    else:
        insert_one_result = col.insert_one(data)
        return insert_one_result
        
