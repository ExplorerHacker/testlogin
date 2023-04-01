from instagram.models import Instagram_Account
from django import forms

class Instagram_Account_Form(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     
     class Meta:
          model = Instagram_Account
          fields = '__all__'
          
     
          
          

