from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.nombre} {self.apellidos}, {self.email}'



class Suscripcion(models.Model):
    suscripcion_email = models.EmailField()

    def __str__(self):
        return f'Suscripción de {self.cliente.email}'