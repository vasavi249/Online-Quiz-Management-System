from rest_framework.decorators import api_view
from rest_framework.response import Response
from db import (
    students_collection, quizzes_collection, questions_collection,
    attempts_collection, results_collection, serialize_doc
)
from bson.objectid import ObjectId

# ================= STUDENTS =================
@api_view(['POST'])
def add_student(request):
    res = students_collection.insert_one(request.data)
    return Response({"message": "Student added", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_students(request):
    students = list(students_collection.find())
    return Response([serialize_doc(s) for s in students])

@api_view(['PUT'])
def update_student(request, id):
    students_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Student updated"})

@api_view(['DELETE'])
def delete_student(request, id):
    students_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Student deleted"})

# ================= QUIZZES =================
@api_view(['POST'])
def add_quiz(request):
    res = quizzes_collection.insert_one(request.data)
    return Response({"message": "Quiz added", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_quizzes(request):
    quizzes = list(quizzes_collection.find())
    return Response([serialize_doc(q) for q in quizzes])

@api_view(['PUT'])
def update_quiz(request, id):
    quizzes_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Quiz updated"})

@api_view(['DELETE'])
def delete_quiz(request, id):
    quizzes_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Quiz deleted"})

# ================= QUESTIONS =================
@api_view(['POST'])
def add_question(request):
    res = questions_collection.insert_one(request.data)
    return Response({"message": "Question added", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_questions(request):
    questions = list(questions_collection.find())
    return Response([serialize_doc(q) for q in questions])

@api_view(['PUT'])
def update_question(request, id):
    questions_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Question updated"})

@api_view(['DELETE'])
def delete_question(request, id):
    questions_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Question deleted"})

# ================= ATTEMPTS =================
@api_view(['POST'])
def add_attempt(request):
    res = attempts_collection.insert_one(request.data)
    return Response({"message": "Attempt saved", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_attempts(request):
    attempts = list(attempts_collection.find())
    return Response([serialize_doc(a) for a in attempts])

@api_view(['PUT'])
def update_attempt(request, id):
    attempts_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Attempt updated"})

@api_view(['DELETE'])
def delete_attempt(request, id):
    attempts_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Attempt deleted"})

# ================= RESULTS =================
@api_view(['POST'])
def add_result(request):
    res = results_collection.insert_one(request.data)
    return Response({"message": "Result saved", "id": str(res.inserted_id)})

@api_view(['GET'])
def get_results(request):
    results = list(results_collection.find())
    return Response([serialize_doc(r) for r in results])

@api_view(['PUT'])
def update_result(request, id):
    results_collection.update_one({"_id": ObjectId(id)}, {"$set": request.data})
    return Response({"message": "Result updated"})

@api_view(['DELETE'])
def delete_result(request, id):
    results_collection.delete_one({"_id": ObjectId(id)})
    return Response({"message": "Result deleted"})
