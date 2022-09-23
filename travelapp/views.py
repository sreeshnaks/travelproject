from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from travelapp.models import place


def fun(request):
   obj=place.objects.all()
   return render(request,"index.html",{'results':obj})

