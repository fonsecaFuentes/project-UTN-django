from django.urls import path
from app_user import views

urlpatterns = [
    path('app_user/', views.register, name='register'),
    path('app_user/', views.user_login, name='login'),
]
