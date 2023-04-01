from django.urls import path
from instagram.views import Instagram_Account_View

urlpatterns = [
    path('instagram/', Instagram_Account_View, name="instagram"),
]
