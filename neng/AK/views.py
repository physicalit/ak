from django.shortcuts import render
from .models import Slider 

# Create your views here.
def figma_view(request):
    slider = Slider.objects.all()
    return render(request, 'AK/index.html', {'slider': slider}) 
def figma_prods(request):
    return render(request, 'AK/productpage.html') 