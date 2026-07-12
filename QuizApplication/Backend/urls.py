from django.urls import path
import views

urlpatterns = [
    # Students
    path('students/add/', views.add_student),
    path('students/', views.get_students),
    path('students/update/<str:id>/', views.update_student),
    path('students/delete/<str:id>/', views.delete_student),
    
    # Quizzes
    path('quizzes/add/', views.add_quiz),
    path('quizzes/', views.get_quizzes),
    path('quizzes/update/<str:id>/', views.update_quiz),
    path('quizzes/delete/<str:id>/', views.delete_quiz),
    
    # Questions
    path('questions/add/', views.add_question),
    path('questions/', views.get_questions),
    path('questions/update/<str:id>/', views.update_question),
    path('questions/delete/<str:id>/', views.delete_question),
    
    # Attempts
    path('attempts/add/', views.add_attempt),
    path('attempts/', views.get_attempts),
    path('attempts/update/<str:id>/', views.update_attempt),
    path('attempts/delete/<str:id>/', views.delete_attempt),
    
    # Results
    path('results/add/', views.add_result),
    path('results/', views.get_results),
    path('results/update/<str:id>/', views.update_result),
    path('results/delete/<str:id>/', views.delete_result),
]
