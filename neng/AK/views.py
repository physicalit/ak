from django.shortcuts import render
from .models import Slider, Footer

# Create your views here.
def figma_view(request):
    slider = Slider.objects.all()
    footer = Footer.objects.first()
    return render(request, 'AK/index.html', {'slider': slider, 'footer': footer}) 
def figma_prods(request):
    footer = Footer.objects.first()
    return render(request, 'AK/productpage.html', {'footer': footer}) 