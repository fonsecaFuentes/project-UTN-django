from django.urls import path
from .views import ListCoupling
from couplings import views

urlpatterns = [
    path('coupling/', ListCoupling.as_view(), name='coupling'),
    path(
        '<int:coupling_id>/coupling/',
        views.coupling_detail,
        name='coupling_detail'
    ),
    path(
        'pumps/add_coupling/<int:pump_id>/<int:motor_id>',
        views.add_coupling, name='add_coupling'
    ),
    path(
        'pumps/add_coupling_list',
        views.add_coupling_list,
        name='add_coupling_list'
    )
]
