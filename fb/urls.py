from django.urls import path
from fb.views import fvbView

urlpatterns = [
     path('fb/', fvbView),
]