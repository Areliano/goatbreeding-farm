from django.shortcuts import render
from .models import Homepage

def homepage(request):
    homepage = Homepage.objects.first()
    return render(request, 'breedingfarm/homepage.html', {'homepage': homepage, 'nav': 'homepage'})

def about(request):
    return render(request, 'breedingfarm/about.html', {'nav': 'about'})

def breeds(request):
    return render(request, 'breedingfarm/breeds.html', {'nav': 'breeds'})

def services(request):
    return render(request, 'breedingfarm/services.html', {'nav': 'services'})

def gallery(request):
    return render(request, 'breedingfarm/gallery.html', {'nav': 'gallery'})

def blog(request):
    return render(request, 'breedingfarm/blog.html', {'nav': 'blog'})

def contact(request):
    return render(request, 'breedingfarm/contact.html', {'nav': 'contact'})
