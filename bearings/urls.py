from django.urls import path
from .views import ListBearings
from bearings import views

urlpatterns = [
    path('bearings/', ListBearings.as_view(), name='bearings'),
    path(
        '<int:bearing_id>/bearing/',
        views.bearing_detail,
        name='bearing_detail'
    )
]
