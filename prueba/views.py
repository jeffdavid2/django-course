from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def home(request):
    return render(request, 'prueba/index.html')

def contact(request):
    return render(request, 'prueba/contacto.html')

def about(request):
    return render(request, 'prueba/about.html')

def login(request):
    return render(request, 'prueba/login.html')


