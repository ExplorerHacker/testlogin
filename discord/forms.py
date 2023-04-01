from discord.models import Discord_Account
from django import forms

class Discord_Account_Form(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     
     class Meta:
          model = Discord_Account
          fields = '__all__'
          
     
          
          

