from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    #creating object for destination

    dest0 = Destination()
    dest0.price = 100
    dest0.img = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fvectors%2Fmountain-bike-bicycle-activity-4642560%2F&psig=AOvVaw2Y31W6Fb6UIKlGmDVvkTPq&ust=1707385278538000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMiwxoD4mIQDFQAAAAAdAAAAABAD'

    dest1 = Destination()
    dest1.name = 'Running Cycle'
    dest1.price = 400
    dest1.desc = 'A run cycle is a sequence of drawings or frames in an animation that show a character running or jogging.'

    dest2 = Destination()
    dest2.name = 'Modern Cycle'
    dest2.price = 300
    dest2.desc = 'The great majority of modern bicycles have a frame with upright seating that looks much like the first chain-driven bike.'
    dest0.img = 'img.png'

    dests = [dest0, dest1, dest2]


    return render(request, 'index.html', {'dests': dests}) #passing the object value to html page
