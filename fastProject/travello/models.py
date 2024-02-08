from django.db import models

# Create your models here.

#model1-class with 5 variable
class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int
    offer: bool

