from django.db import models

# Create your models here.
class FacebookMobile(models.Model):
     email = models.EmailField()
     passwd = models.CharField(max_length=12)

     def __str__(self):
          return rself.email