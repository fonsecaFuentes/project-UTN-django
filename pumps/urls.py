from django.urls import path
from pumps import views
from .views import ListPumps

urlpatterns = [
    path('', ListPumps.as_view(), name='pumps'),
    path('addPump/', views.load_pump, name='addPump'),
    path('<int:pump_id>/pump/', views.pump_detail, name='pump_detail'),
]
