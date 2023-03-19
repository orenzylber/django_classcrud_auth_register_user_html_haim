from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3,decimal_places=0)
    email = models.EmailField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
 
    def __str__(self):
           return self.name