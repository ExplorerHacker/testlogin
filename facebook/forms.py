from .models import Facebook_Account
from django import forms

class Facebook_Account_Form(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     
     class Meta:
          model = Facebook_Account
          fields = '__all__'
          
     
          
          

