from django.shortcuts import render
from .models import Slider, Footer, AboutUs, IndexParagraph

# Create your views here.
def figma_view(request):
    slider = Slider.objects.first()
    footer = Footer.objects.first()
    aboutUs = AboutUs.objects.first()
    indexp = IndexParagraph.objects.first()
    context = {'slider': slider, 'footer': footer, 'aboutus': aboutUs, 'indexp': indexp}
    return render(request, 'AK/index.html', context) 
def figma_prods(request):
    footer = Footer.objects.first()
    return render(request, 'AK/productpage.html', {'footer': footer}) 