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
]
