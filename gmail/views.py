from django.shortcuts import render
from gmail.models import Gmail_Accounts
from gmail.forms import Gmail_Account_Form
# Create your views here.

def gmailView(request):
     form = Gmail_Account_Form
     context = {'form': form}
     return render(request, "gmail.html", context)
