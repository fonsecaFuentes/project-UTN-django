from django.urls import path
from .views import ListMotors
# from motors import views

urlpatterns = [
    path('motors/', ListMotors.as_view(), name='motors'),
]
