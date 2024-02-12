from django.db import models
from django.db.models import Model

# Create your models here.

#model1-class with 5 variable
class Destination(models.Model): #convert the class into a model basically inheritence the feature of models here    
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

