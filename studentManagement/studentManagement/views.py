from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Home is Here....")
    return render(request, "index.html")

def about(request):
    return HttpResponse("about is Here....")

def contact(request):
    return HttpResponse("contact is Here....")