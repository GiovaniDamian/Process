from django.shortcuts import render
from django.http import HttpRequest
from .models import telzir

# Create your views here.

def index(request):
    products = telzir.objects.all()
    return render(request, 'index.html',
                  {'products': products})




