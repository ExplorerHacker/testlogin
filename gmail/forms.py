from .models import Gmail_Accounts
from django import forms

class Gmail_Account_Form(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     
     class Meta:
          model = Gmail_Accounts
          fields = '__all__'
          
     
          
          

