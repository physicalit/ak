from django.shortcuts import render, redirect
from .models import Slider, Footer, AboutUs, IndexParagraph, ContactSubmission, Product
from .forms import ContactForm

# Create your views here.
def figma_view(request):
    slider = Slider.objects.first()
    footer = Footer.objects.first()
    aboutUs = AboutUs.objects.first()
    indexp = IndexParagraph.objects.first()
    products = Product.objects.all()
    context = {'slider': slider, 'footer': footer, 'aboutus': aboutUs, 'indexp': indexp, 'products': products}
    return render(request, 'index.html', context) 
def figma_prods(request):
    footer = Footer.objects.first()
    return render(request, 'productpage.html', {'footer': footer}) 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message = form.cleaned_data['message']

            # Save the data to the database   

            submission = ContactSubmission(name=name, email=email, message=message)
            submission.save() 

            return render(request, 'index.html', {'formst': 'was successful!'})  # Render a success template
        else:
            return render(request, 'index.html', {'formst': 'has failed!'})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form}) 