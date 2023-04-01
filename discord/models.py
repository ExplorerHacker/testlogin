from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Discord_Account(models.Model):
     email = models.EmailField(max_length=254)
     phone_number = PhoneNumberField(blank=True)
     password = models.CharField(max_length=50)
     
     def __str__(self):
          return self.password
          
          
