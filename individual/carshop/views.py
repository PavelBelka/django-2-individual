from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Car, Purchase, Equipment, Engine, Transmission


#from .serializers import ProductSerializer
# Create your views here.


def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'shop/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')


def configurator(request, ids, step, complid):
    global price
    step += 1
    if step == 1:
        price = 0
        main = Car.objects.get(id=ids)
        complection = Equipment.objects.filter(car__id=ids)
        return render(request, 'shop/Configurator.html', {'Names': main,'car_id':ids, 'Steps': step, 'Cost':price, 'Compl':complection})
    if step == 2:
        price += Equipment.objects.get(id=complid).cost
        main = Car.objects.get(id=ids)
        complection= Engine.objects.filter(equipment__id=complid)
        return render(request, 'shop/Configurator.html', {'Names': main, 'car_id': ids, 'Steps': step, 'Cost': price, 'Compl': complection})
    if step == 3:
        price += Engine.objects.get(id=complid).cost
        main = Car.objects.get(id=ids)
        complection = Transmission.objects.filter(engine__id=complid)
        return render(request, 'shop/Configurator.html', {'Names': main, 'car_id': ids, 'Steps': step, 'Cost': price, 'Compl': complection})
    if step == 4:
        price += Transmission.objects.get(id=complid).cost
        main = Car.objects.get(id=ids)
        return render(request, 'shop/Configurator.html', {'Names': main, 'car_id': ids, 'Steps': step, 'Cost': price})

def my_purchase(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    model = Purchase.objects.filter(user = username)
    return render(request, 'shop/purchase.html', {'purchase': model})

def PurchaseCreate(request, car_id, costs):
    purc = Purchase()
    purc.price = costs
    purc.user = request.user.username
    purc.car =  Car.objects.get(id=car_id)
    purc.save()
    return HttpResponse(f'Спасибо за покупку!')
