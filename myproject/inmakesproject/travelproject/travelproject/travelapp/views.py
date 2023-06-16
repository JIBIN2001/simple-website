from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import People


# Create your views here.

def place(request):
    place = Place.objects.all()
    people = People.objects.all()
    return render(request,"index.html",{'result1':place,'result2':people})

