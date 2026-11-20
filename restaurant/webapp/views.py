from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def administration(request):
    return render(request, 'administration.html')

def contact(request):
    return render(request, 'contact.html')
