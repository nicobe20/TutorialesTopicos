from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)  
    historial_compras = models.TextField()  
    opiniones = models.TextField() 
