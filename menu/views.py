from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    breakfast = Breakfast.objects.all()
    lunch = LunchDinner.objects.all()
    starter = Starter.objects.all()
    salads = Salad.objects.all()
    drinks = Drink.objects.all()
    context={
        'breakfast':breakfast,
        'lunch':lunch,
        'starter':starter,
        'salads':salads,
        'drinks':drinks,
        
        }
    return render(request,'menu/index.html',context)