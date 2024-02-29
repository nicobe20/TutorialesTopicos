from django.test import TestCase
from django.core.validators import RegexValidator
# Create your tests here.

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length = 50)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(validators=[RegexValidator(regex='^.{6}$', message='la contraseña tiene que tener minimo 6 caracteres', code='nomatch')])
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)  
    historial_compras = models.TextField()  
    opiniones = models.TextField()  

    def __str__(self):
        return self.nombre

    def comprar(self):
        # Método para realizar una compra, podrías implementar la lógica aquí
        pass

    def opinar(self):
        # Método para dejar una opinión, podrías implementar la lógica aquí
        pass

    def ver_historial_compras(self):
        # Método para ver el historial de compras, podrías implementar la lógica aquí
        pass

    def ver_recomendaciones(self):
        # Método para ver las recomendaciones, podrías implementar la lógica aquí
        pass
