from django.urls import path
from webmail.views import WebmailView

urlpatterns = [
     path('webmail/', WebmailView, name="webmail")
]