from rest_framework.decorators import api_view
from rest_framework.response import Response
from db import (
    users_collection, chats_collection, serialize_doc
)
from bson.objectid import ObjectId

# ================= USERS =================
@api_view(['POST'])
def register_user(request):
    res = users_collection.insert_one(request.data)
    return Response({"message": "User registered", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_users(request):
    users = list(users_collection.find())
    return Response([serialize_doc(u) for u in users])

@api_view(['PUT'])
def update_user(request, id):
    users_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "User updated"})

@api_view(['DELETE'])
def delete_user(request, id):
    users_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "User deleted"})


# ================= CHATS =================
@api_view(['POST'])
def send_chat(request):
    res = chats_collection.insert_one(request.data)
    return Response({"message": "Message sent", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_chats(request):
    chats = list(chats_collection.find())
    return Response([serialize_doc(c) for c in chats])

@api_view(['PUT'])
def update_chat(request, id):
    chats_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Message updated"})

@api_view(['DELETE'])
def delete_chat(request, id):
    chats_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Message deleted"})


# ================= CONVERSATION =================
@api_view(['GET'])
def get_conversation_all(request):
    chats = list(chats_collection.find())
    return Response([serialize_doc(c) for c in chats])

@api_view(['GET'])
def get_conversation_user(request, username):
    # Find chats where the user is either sender or receiver
    query = {
        "$or": [
            {"sender": username},
            {"receiver": username}
        ]
    }
    chats = list(chats_collection.find(query).sort("sent_at", 1))
    return Response([serialize_doc(c) for c in chats])
