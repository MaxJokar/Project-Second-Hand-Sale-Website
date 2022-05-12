from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader

# Create your views here. 1 style for  return is given blown:
def index(request):
    return HttpResponse("<h1 style='color:red;' >My first page index  and space is ready</h1>")

def step1(request):
    return HttpResponse("<h1 style='color:red;' >My STEP 1 is ready</h1>")
    # template=loader.get_template('mainapp/mainPageSite.html')
    # return HttpResponse(template.render())
    
def blog(request):
    return HttpResponse("<h1 style='color:red;' >My Blog 1 is ready</h1>")
    
    
    
    
    