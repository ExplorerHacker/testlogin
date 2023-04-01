from django.urls import path
from gmail.views import gmailView

urlpatterns = [
    path('email/', gmailView, name="gmail"),
] 
