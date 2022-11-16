from django.db import models

# Create your models here.
from tkinter.tix import INTEGER
from unicodedata import name
from django.db import models
import os
import datetime

def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)
class Record(models.Model):
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    pimage=models.ImageField(upload_to=filepath,null=True,blank=True)

class BlogData(models.Model):
    title=models.CharField(max_length=50)
    data=models.TextField()
    image=models.ImageField(upload_to=filepath,null=True,blank=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    datetime=models.DateTimeField()


class savemsg(models.Model):
    uname=models.CharField(max_length=50)
    uemail=models.CharField(max_length=50)
    usub=models.CharField(max_length=50)
    umsg=models.CharField(max_length=50)
   





# class product(models.Model):
    
#    image=models.ImageField(upload_to=filepath,null=True,blank=True)
#    name=models.CharField(max_length=20)  
#    size=models.CharField(max_length=20)


    
def __str__(self):
    return self.name
    
