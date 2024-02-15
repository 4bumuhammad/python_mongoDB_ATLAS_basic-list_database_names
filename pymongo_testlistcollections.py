from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://mugjkt:mugjkt@cluster0.oeh2p2u.mongodb.net/"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Pilih database "sample_analytics"
    database_name = "sample_analytics"
    db = client[database_name]

    # Dapatkan daftar nama-nama koleksi (collections)
    collection_names = db.list_collection_names()

    # Buat JSON object
    collections_json = {"collections": collection_names}

    # Tampilkan daftar nama-nama koleksi dalam bentuk JSON
    print(json.dumps(collections_json, indent=2))

except Exception as e:
    print(f"Failed to connect to MongoDB. Error: {e}")
