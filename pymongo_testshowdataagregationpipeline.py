from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from bson import json_util 

uri = "mongodb+srv://mugjkt:mugjkt@cluster0.oeh2p2u.mongodb.net/"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
database_name = "sample_analytics"
collection_name = "customers"

db = client[database_name]
collection = db[collection_name]

pipeline = [
  {
    "$match": {
      "active": True
    }
  },
  {
    "$project": {
      "username": 1,
      "name": 1,
      "address": 1,
      "totalAccounts": { "$size": { "$ifNull": ["$accounts", []] } },
    }
  }
]

result = list(collection.aggregate(pipeline))

for doc in result:
    data_str = json.dumps(doc, indent=2, default=json_util.default)
    print(data_str)