from urllib.parse import quote
from pymongo import MongoClient

# the local connection
port = 27017
host = 'localhost'
client = MongoClient(host, port)

# the remote connection
socket_path = 'cluster0.anhr9.mongodb.net/'
user = 'chuckvanhoff'
password = quote('Fe7ePrX!5L5Wh6W') # url encode the password for the mongodb uri
uri = "mongodb+srv://%s:%s@%s" % (user, password, socket_path)
### SOMETHING NEEDS TO BE HERE TO ENSURE THIS LINE DOES NOT STIMY THE
### CONNECTION ATTEMPT...AS IT IS NOW, WITHOUT INTERNET ACCESS, IT ENDS HERE.
remote_client = MongoClient(uri)

# database and collection names
database = 'owm_test'
# database = 'main_test'
# database = 'owm_11022020'
collection = 'owm_test'
weathers_collection = 'weather_temp'
weathers_archive = 'archive'
observation_collection = 'obs_temp'
forecast_collection = 'cast_temp'
instants_collection = 'inst_temp'
legit_instants = 'legit_inst'

cron_limit = None
test_limit = 1000


print(f'imported config from {__file__}')
