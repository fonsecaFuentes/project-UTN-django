from django.urls import path
from .views import ListSeals
from seals import views

urlpatterns = [
    path('seals/', ListSeals.as_view(), name='seals'),
    path('<int:seal_id>/seal/', views.seal_detail, name='seal_detail')
]
