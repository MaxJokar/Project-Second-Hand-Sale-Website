import imp
# from multiprocessing import context
from django.shortcuts import render
from django.http import  HttpResponse
# from django.template import loader
#To use  Css or Html we add the import Belown:
from django.conf import settings
# 1st style for  RETURN  is given blown:
# from django.shortcuts import render
from django.template import context




def car(request):
    context={
        'media_url':settings.MEDIA_URL 
    }
    return render(request,'blog/cars/car.html',context)



import os
def cars(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images')
        
    context={
        'media_url':settings.MEDIA_URL,
        "imageList":imageList
        # imageName:'',
        
    }
    
    return render(request,'blog/cars/cars.html',context)










def index(request):
    return HttpResponse("<h1 style='color:red;' >My first page index  and space is ready</h1>")

#2nd type of RETURN given Blown (one more option )
def step1(request):
    return HttpResponse("<h1 style='color:red;' >My STEP1  is ready</h1>")
    # template=loader.get_template('mainapp/mainPageSite.html')
    # return HttpResponse(template.render())
    
def blog1(request):
    return HttpResponse("<h1 style='color:red;' >My Blog blog 1 is ready</h1>")
    
def blog2(request):
    return HttpResponse("<h1 style='color:red;' >My Blog blog 2 is ready</h1>")
       


























    
    