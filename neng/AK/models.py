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
    
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=650)
    
class IndexParagraph(models.Model):
    content1 = models.CharField(max_length=650)
    content2 = models.CharField(max_length=650)
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    link_specs = models.CharField(max_length=150, default="link_pdf_placeholder")
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    specifications = models.JSONField(default=list) 
    PRODUCT_TYPE_CHOICES = (
        ('hardware', 'Hardware Products'),
        ('software', 'Software Products '),
        ('services', 'Services'),
        ('promotions', 'Promotions'))
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES, default='physical')
    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)