"""sh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from apps.blog.views import index,step1,blog1
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    
    path('admin/', admin.site.urls),
    # path('', index),#if we dont have any other Folder in Apps folder
    path('', include('apps.blog.urls')),#index implements
    # path('step/',include('apps.blog.urls')),because it goes to blog Folder urls.py we can have all urls connected to views in block Blog
    path('gallery/',include('apps.blog.urls')),
    #/blog/carsPhoto/
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# to have a iamge we should add above syntax: to have folder Media we should get authorization we get it by the syntax above:









