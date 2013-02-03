#from flask import Flask
from mongokit import Connection, Document

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('db.ini')

# configuration
# mongohq
MONGODB_HOST = config.get('default', 'host')
MONGODB_PORT = config.get('default', 'port')
MONGODB_USER = config.get('default', 'username')
MONGODB_PASS = config.get('default', 'pass')
MONGODB_DB = config.get('default', 'dbname')

host = 'mongodb://%s:%s@%s:%s/%s' % (MONGODB_USER, MONGODB_PASS, MONGODB_HOST, MONGODB_PORT, MONGODB_DB)

# create the little application object
#app = Flask(__name__)
#app.config.from_object(__name__)

# connect to the database
connection = Connection(host=host)
