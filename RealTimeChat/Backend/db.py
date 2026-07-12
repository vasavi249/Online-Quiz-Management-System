import pymongo
from bson.objectid import ObjectId

# Local MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["realtime_chat_app"]

# Collections
users_collection = db["users"]
chats_collection = db["chats"]

def serialize_doc(doc):
    if not doc:
        return None
    if "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc
