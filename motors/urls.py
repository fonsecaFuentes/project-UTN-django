from django.urls import path
from motors import views

urlpatterns = [
    path('motors/', views.motors, name='motors'),
]
