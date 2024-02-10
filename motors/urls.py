from django.urls import path
from .views import ListMotors
from motors import views

urlpatterns = [
    path('motors/', ListMotors.as_view(), name='motors'),
    path('<int:motor_id>/motor/', views.motor_detail, name='motor_detail'),
]
