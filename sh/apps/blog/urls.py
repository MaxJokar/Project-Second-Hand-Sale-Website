from django.urls import path
import apps.blog.views as views  #we shorten using as instead of writing a long text




urlpatterns=[
    # path('',views.index),
    path('',views.car),
    path('step1/',views.step1),
    # path('blog1/',views.blog1),
    # path('blog2/',views.blog2),
    path('car/',views.car,name="templatecar"),
    path('cars/',views.cars,name="templatecars"),
      
]      