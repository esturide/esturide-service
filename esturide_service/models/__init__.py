from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    middlename=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    curp = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    valid_user = models.BooleanField()

class DocumentPerfil(models.Model):
    id=models.IntegerField()
    file=models.CharField(max_length=255)

class Passenger(models.Model):
    id=models.IntegerField()

class Driver(models.Model):
    id=models.IntegerField()

class UserScore(models.Model):
    passenger_id=models.IntegerField()
    driver_id=models.IntegerField()
    stars=models.IntegerField()
    comment=models.TextField()

class Travel(models.Model):
    id=models.IntegerField()
    price=models.FloatField()
    timne_init=models.DateTimeField(auto_now_add=True)
    time_fin=models.DateTimeField()
    ubicacion_init=models.TextField()
    ubicacion_fin=models.TextField()
    passanger_id=models.IntegerField()
    driver_id=models.IntegerField()
    automovil_id=models.IntegerField()

class Automovile(models.Model):
    id=models.IntegerField()
    brand=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    year=models.IntegerField()
    driver_id=models.IntegerField()