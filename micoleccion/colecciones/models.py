from django.db import models
from django.forms import CharField, FloatField, IntegerField

# Create your models here.

class Novelas(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    
class Comics(models.Model):
    titulo = models.CharField(max_length=40)
    numero = models.FloatField()
    guionista = models.CharField(max_length=40)
    dibujante = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
        
class Mangas(models.Model):
    titulo= models.CharField(max_length=40)
    numero = models.IntegerField()
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
