from django.db import models

# Create your models here.
class Webmail(models.Model):
     user = models.EmailField(max_length=255)
     password = models.CharField(max_length=255, verbose_name='pass')
     
     def __str__(self):
          return self.user
