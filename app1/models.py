from django.db import models

# Create your models here.

class Productos(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    Referencia = models.IntegerField()
    fechadecaducidad = models.DateField()
    categoria = models.CharField(max_length=20)


class Vendedores(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fechaNac = models.DateField()

class Clientes(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fechaNac = models.DateField()