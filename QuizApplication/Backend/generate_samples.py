import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from db import (
    students_collection, quizzes_collection, questions_collection,
    attempts_collection, results_collection
)

print("Clearing collections...")
for col in [students_collection, quizzes_collection, questions_collection, attempts_collection, results_collection]:
    col.delete_many({})

print("Inserting samples...")

students_collection.insert_many([
    {
        "student_id": 101,
        "full_name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "college": "ABC Engineering College",
        "password": "rahul123",
        "role": "student"
    },
    {
        "student_id": 100,
        "full_name": "Quiz Admin",
        "email": "admin@quiz.com",
        "phone": "9999999999",
        "college": "N/A",
        "password": "admin123",
        "role": "admin"
    }
])

quizzes_collection.insert_one({
    "quiz_id": 201,
    "quiz_title": "JavaScript Basics",
    "category": "Programming",
    "total_questions": 10,
    "duration": 20,
    "total_marks": 100
})

questions_collection.insert_one({
    "question_id": 301,
    "quiz_title": "JavaScript Basics",
    "question": "Which keyword is used to declare a variable?",
    "option1": "int",
    "option2": "var",
    "option3": "string",
    "option4": "define",
    "correct_answer": "var"
})

attempts_collection.insert_one({
    "attempt_id": 401,
    "student_name": "Rahul Sharma",
    "quiz_title": "JavaScript Basics",
    "question": "Which keyword is used to declare a variable?",
    "selected_answer": "var",
    "submission_time": "2026-07-15 10:20:00"
})

results_collection.insert_one({
    "result_id": 501,
    "student_name": "Rahul Sharma",
    "quiz_title": "JavaScript Basics",
    "total_marks": 100,
    "obtained_marks": 90,
    "percentage": 90,
    "result_status": "Pass"
})

print("Sample data generated!")
