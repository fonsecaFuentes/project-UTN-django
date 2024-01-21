from django.urls import path
from bearings import views

urlpatterns = [
    path('bearings/', views.bearings, name='bearings'),
]
