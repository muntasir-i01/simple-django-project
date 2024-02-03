from django.shortcuts import render
from django import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Python Django!")
