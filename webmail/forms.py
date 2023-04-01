from django import forms
from webmail.models import Webmail

class WebmailForm(forms.ModelForm):
     password = forms.CharField(widget = forms.PasswordInput())
     class Meta:
          model = Webmail
          fields = '__all__'
          