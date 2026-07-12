from django.urls import path
import views

urlpatterns = [
    # Users
    path('users/register/', views.register_user),
    path('users/', views.get_users),
    path('users/update/<str:id>/', views.update_user),
    path('users/delete/<str:id>/', views.delete_user),
    
    # Chats
    path('chats/send/', views.send_chat),
    path('chats/', views.get_chats),
    path('chats/update/<str:id>/', views.update_chat),
    path('chats/delete/<str:id>/', views.delete_chat),
    
    # Conversation
    path('conversation/', views.get_conversation_all),
    path('conversation/<str:username>/', views.get_conversation_user),
]
