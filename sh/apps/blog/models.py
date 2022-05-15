from django.db import models

#1.Create your models here 
from django.utils import timezone



#4 make a Model then        makemigrations migrate           etc!
class Author(models.Model):
    
    name=models.CharField(max_length=30)
    family=models.CharField(max_length=30)
    slug=models.SlugField(max_length=100)
    age=models.IntegerField(default=20)
    is_active=models.BooleanField(default=True)
    register_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=100)
    image_name=models.CharField(max_length=200,default='nophoto',null=True,blank='True')
    
    
    def __str__(self) :  # To see the Datas in usual way :
        return f"{self.name}\t{self.family}\t{self.age}"


















