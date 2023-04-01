from django.shortcuts import render
from webmail.forms import WebmailForm
from webmail.models import Webmail
# Create your views here.

def WebmailView(request):
     form = WebmailForm()
     if request.method == 'POST':
          form - WebmailForm(request.POST)
          if form.is_valid():
               form.save()
     context = {'form': form}
     return render(request, "WebmailLogin.html", context)
