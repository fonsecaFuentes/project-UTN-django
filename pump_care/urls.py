from django.urls import path
from pump_care import views

urlpatterns = [
    path('', views.index, name='home'),
    path("logout/", views.exit, name='logout'),
]
