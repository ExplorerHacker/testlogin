# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from facebook.views import Facebook_Account_View

urlpatterns = [
    path('facebook/', Facebook_Account_View, name="facebook"),
] 
