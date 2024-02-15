from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from bson import json_util 

uri = "mongodb+srv://mugjkt:mugjkt@cluster0.oeh2p2u.mongodb.net/"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Pilih database "sample_analytics"
    database_name = "sample_analytics"
    db = client[database_name]

    # Pilih koleksi "customers"
    collection_name = "customers"
    collection = db[collection_name]

    # Dapatkan semua data dalam koleksi "customers"
    all_customer_data = collection.find()

    # Tampilkan semua data dalam bentuk JSON
    for data in all_customer_data:
        # Convert ObjectId to string before JSON serialization
        data_str = json.dumps(data, indent=2, default=json_util.default)
        print(data_str)

except Exception as e:
    print(f"Failed to connect to MongoDB. Error: {e}")