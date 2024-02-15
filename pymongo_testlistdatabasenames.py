from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://mugjkt:mugjkt@cluster0.oeh2p2u.mongodb.net/"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Dapatkan daftar nama-nama database
    database_names = client.list_database_names()

    # Buat JSON object
    database_names_json = {"database_names": database_names}

    # Tampilkan daftar nama-nama database dalam bentuk JSON
    print(json.dumps(database_names_json, indent=2))

except Exception as e:
    print(f"Failed to connect to MongoDB. Error: {e}")
