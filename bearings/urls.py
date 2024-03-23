from django.urls import path
from .views import ListBearings
from .views import AddBearingView
from bearings import views

urlpatterns = [
    path('bearings/', ListBearings.as_view(), name='bearings'),
    path(
        '<int:bearing_id>/bearing/',
        views.bearing_detail,
        name='bearing_detail'
    ),
    path(
        'add_bearing/<int:pump_id>',
        AddBearingView.as_view(),
        name='add_bearing'
    ),
    # path(
    #     'add_bearing/<int:motor_id>',
    #     views.add_bearing,
    #     name='add_bearing_motor'
    # ),
    path('add_bearing/', views.add_bearing, name='add_bearing')
]
