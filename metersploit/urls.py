from django.urls import path
from .views import meterView


urlpatterns = [
    path('metersploit/', meterView, name="metersploit"),
] 