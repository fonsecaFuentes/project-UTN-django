from django.urls import path
from seals import views

urlpatterns = [
    path('seals/', views.seals, name='seals'),
]
