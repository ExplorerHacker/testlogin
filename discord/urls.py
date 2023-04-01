from django.urls import path
from discord.views import Discord_Account_View

urlpatterns = [
    path('discord/', Discord_Account_View),
] 
