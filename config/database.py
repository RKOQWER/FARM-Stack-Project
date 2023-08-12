# import statement

from pymongo import MongoClient

# create db connection
db_url="mongodb://localhost:27017/test"

connection=MongoClient(db_url)

