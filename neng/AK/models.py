from django.db import models

# Create your models here.
class Slider(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    
class Footer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
