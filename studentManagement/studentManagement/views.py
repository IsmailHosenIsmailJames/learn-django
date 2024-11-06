from django.http import HttpResponse

def home(request):
    return HttpResponse("Home is Here....")

def about(request):
    return HttpResponse("about is Here....")

def contact(request):
    return HttpResponse("contact is Here....")