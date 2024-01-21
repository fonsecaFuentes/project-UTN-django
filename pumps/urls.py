from django.urls import path
from pumps import views

urlpatterns = [
    path('', views.pumps, name='pumps'),
]
