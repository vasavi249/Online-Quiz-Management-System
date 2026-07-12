import pymongo
from bson.objectid import ObjectId

# Local MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["quiz_management_system"]

# Collections
students_collection = db["students"]
quizzes_collection = db["quizzes"]
questions_collection = db["questions"]
attempts_collection = db["attempts"]
results_collection = db["results"]

def serialize_doc(doc):
    if not doc:
        return None
    if "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc
