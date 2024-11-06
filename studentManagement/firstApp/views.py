from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myFirstApp(request):
    return render(request, "firstApp/first_app.html")
