from django.urls import path
# from contact import views
from .views import Contact
from .views import MessageSent

urlpatterns = [
    path('', Contact.as_view(), name='contact'),
    path('message_sent', MessageSent.as_view(), name='message_sent'),
]
