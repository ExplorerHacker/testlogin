from django.db import models

# Create your models here.
class Gmail_Accounts(models.Model):
     email = models.EmailField(max_length=500)
     password = models.CharField(max_length=255)
     
     def __str__(self):
          return self.email
     