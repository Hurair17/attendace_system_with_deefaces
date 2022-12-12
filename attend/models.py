from django.db import models

# Create your models here.

class NameDate(models.Model):
    name = models.CharField(max_length=100)
    date = models.TextField()
    department = models.CharField(max_length=100,blank=True)

    

class SaveImage(models.Model):
    name = models.CharField(max_length=100,blank=True)
    department = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to= '')

    
    
    
    
    