from django.urls import path
from couplings import views

urlpatterns = [
    path('coupling/', views.coupling, name='coupling'),
]
