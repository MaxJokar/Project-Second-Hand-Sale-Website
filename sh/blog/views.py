import imp
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("hello Django , first Django Programm")
    # return HttpResponse("<h1>My first page is ready</h1>")
    return HttpResponse("<h1 style='color:red;' >My first page is ready</h1>")

def page1(request):
    return HttpResponse("My First Page")
