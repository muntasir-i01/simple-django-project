from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    #creating object for destination

    dest0 = Destination()
    dest0.name = 'Kids Cycle'
    dest0.price = 200
    dest0.desc =  'Purchase a kids bicycle of excellent quality for safe cycling for your baby. In 2023, the best childrens bicycle at the best price will be delivered.'
    dest0.img = 'img-4.png'

    dest1 = Destination()
    dest1.name = 'Running Cycle'
    dest1.price = 400
    dest1.desc = 'A run cycle is a sequence of drawings or frames in an animation that show a character running or jogging.'
    dest1.img = 'img-1.png'

    dest2 = Destination()
    dest2.name = 'Modern Cycle'
    dest2.price = 300
    dest2.desc = 'The great majority of modern bicycles have a frame with upright seating that looks much like the first chain-driven bike.'
    dest0.img = 'img-3.png'

    dests = [dest0, dest1, dest2]


    return render(request, 'index.html', {'dests': dests}) #passing the object value to html page
