from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    count = models.IntegerField()

    objects = models.Manager()

class Equipment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    cost = models.IntegerField()

class Engine(models.Model):
    equipment = models.ManyToManyField(Equipment)
    name = models.CharField(max_length=200)
    power = models.IntegerField()
    force = models.IntegerField()
    cost = models.IntegerField()

class Transmission(models.Model):
    engine = models.ManyToManyField(Engine)
    name = models.CharField(max_length=200)
    gear = models.IntegerField()
    drive = models.IntegerField()
    cost = models.IntegerField()

class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)




