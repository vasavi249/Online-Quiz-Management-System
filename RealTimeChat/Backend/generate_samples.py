import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from db import users_collection, chats_collection

print("Clearing collections...")
users_collection.delete_many({})
chats_collection.delete_many({})

print("Inserting samples...")

users_collection.insert_many([
    {
        "user_id": 101,
        "full_name": "Rahul Sharma",
        "username": "rahul",
        "email": "rahul@gmail.com",
        "password": "rahul123",
        "profile_image": "profile.png"
    },
    {
        "user_id": 102,
        "full_name": "Sneha Gupta",
        "username": "sneha",
        "email": "sneha@gmail.com",
        "password": "sneha123",
        "profile_image": "profile.png"
    },
    {
        "user_id": 103,
        "full_name": "Kiran Rao",
        "username": "kiran",
        "email": "kiran@gmail.com",
        "password": "kiran123",
        "profile_image": "profile.png"
    },
    {
        "user_id": 104,
        "full_name": "Arjun Patel",
        "username": "arjun",
        "email": "arjun@gmail.com",
        "password": "arjun123",
        "profile_image": "profile.png"
    }
])

chats_collection.insert_many([
    {
        "chat_id": 1,
        "sender": "rahul",
        "receiver": "sneha",
        "message": "Hello Sneha!",
        "sent_at": "2026-07-10T10:30:00"
    },
    {
        "chat_id": 2,
        "sender": "sneha",
        "receiver": "rahul",
        "message": "Hi Rahul!",
        "sent_at": "2026-07-10T10:31:00"
    },
    {
        "chat_id": 3,
        "sender": "rahul",
        "receiver": "sneha",
        "message": "How are you?",
        "sent_at": "2026-07-10T10:31:30"
    }
])

print("Sample data generated!")
