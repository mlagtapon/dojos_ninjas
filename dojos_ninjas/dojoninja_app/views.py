from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):

    context = {
        "all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas": Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def ninja(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],school_dojo=Dojo.objects.get(name=request.POST['location']))
    return redirect('/')