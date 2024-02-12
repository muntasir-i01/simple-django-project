from django.shortcuts import render
from .models import Destination #we are importing the destination here

# Create your views here.
def index(request):

    dests = Destination.objects.all()

    dest200 = Destination()
    dest200.name = 'Cycling\nto\nSchool'
    dest200.price = 250
    dest200.img = 'img-1.png'
    dest200.id = 5
    dest200.offer = True


    return render(request, 'index.html', {'dests': dests, 'dest200': dest200}) #passing the object value to html page
