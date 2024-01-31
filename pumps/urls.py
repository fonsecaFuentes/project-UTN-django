from django.urls import path
from pumps import views

urlpatterns = [
    path('', views.list_pumps, name='pumps'),
]
