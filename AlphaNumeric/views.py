from django.shortcuts import render
import requests
from AlphaNumeric import templates
# Create your views here.

def index(request):
    return render(request, "index/index.html",{'moreno':''})

def methods(request):
    return render(request, "methods.html",{'moreno':''})

def about(request):
    return render(request, "about.html",{'moreno':''})
