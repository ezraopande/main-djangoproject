from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")


def hello(request):
    return HttpResponse("Hello MIT Class")

def mbote(request):
    return  HttpResponse("This is mbote")

def james(request):
    return  HttpResponse("I am james")

def emobilis(request):
    return  HttpResponse("IThis is emobilis")
