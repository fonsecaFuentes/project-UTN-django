from django.urls import path
from .views import ListMotors
from motors import views

urlpatterns = [
    path('motors/', ListMotors.as_view(), name='motors'),
    path('<int:motor_id>/motor/', views.motor_detail, name='motor_detail'),
    path(
        '<int:pump_id>/add_motor',
        views.add_motor, name='add_motor'
    ),
    path(
        'add_motor_list', views.add_motor_list, name='add_motor_list'
    )
]
