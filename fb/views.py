from django.shortcuts import render

# Create your views here.
def fvbView(request):
     context = {}
     return render(request, 'fb.html', context)