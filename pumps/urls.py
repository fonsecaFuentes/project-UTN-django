from django.urls import path
from pumps import views
from .views import ListPumps
from .views import ListMechanicalSeal
from .views import ListPacking

urlpatterns = [
    path('', ListPumps.as_view(), name='pumps'),
    path('add_pump/', views.load_pump, name='add_pump'),
    path('<int:pump_id>/pump/', views.pump_detail, name='pump_detail'),
    path(
        'mechanical_seals/',
        ListMechanicalSeal.as_view(),
        name='mechanical_seals'
    ),
    path(
        '<int:mechanicalseal_id>/mechanicalSeal/',
        views.mechanicalseal_detail,
        name='mechanicalseal_detail'
    ),
    path('packing/', ListPacking.as_view(), name='packing'),
    path(
        '<int:packing_id>/packing/',
        views.packing_detail,
        name='packing_detail'
        )
]
