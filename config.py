from urllib.parse import quote
from pymongo import MongoClient
from pymongo.errors import ConfigurationError

# the local connection
port = 27017
host = 'localhost'
client = MongoClient(host, port)

# the remote connection
socket_path = 'cluster0.h7tnfll.mongodb.net/'
user = 'mastacow'
password = quote('m!k3bIkE') # url encode the password for the mongodb uri
uri = "mongodb+srv://%s:%s@%s" % (user, password, socket_path)
# remote_client = MongoClient(uri)
try: 
    remote_client = MongoClient(uri)
except ConfigurationError as e:
    print(e)
    print('no remote client')

# database and collection names
database_owm = 'owm_test'
database_wapi = 'wapi_test'
# database = 'main_test'
# database = 'owm_11022020'
collection_owm = 'owm_test'
collection_wapi = 'wapi_test'
weathers_collection = 'weather_temp'
weathers_archive = 'archive'
observation_collection = 'obs_temp'
forecast_collection = 'cast_temp'
instants_collection = 'inst_temp'
legit_instants = 'legit_inst'

cron_limit = None
test_limit = 1000
