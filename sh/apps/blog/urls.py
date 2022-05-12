from django.urls import path
import apps.blog.views as views  #we shorten using as instead of writing a long text




urlpatterns=[
    path('',views.index),
    path('step1/',views.step1),
    path('blog/',views.blog),
      
]      