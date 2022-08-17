from django.db import models

# Create your models here.
class Casa(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField(default=0)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField(default=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Reseña(models.Model):
    nombre = models.CharField(max_length=20)
    reseña = models.TextField()
    
    def __str__(self):
        return self.nombre

class Reservas(models.Model):
    nombrecompleto = models.CharField(max_length=35)
    Telefono = models.IntegerField(default=0)
    Email = models.EmailField(max_length=40)
    Dia_Check_In = models.DateField(auto_now=False)
    Dia_Check_Out  = models.DateField(auto_now=False)
    Adultos = models.IntegerField (default=0)
    Niños = models.IntegerField(default=0)
    Nota = models.TextField()
    def __str__(self):
        return self.nombrecompleto

class Contacto(models.Model):
    nombre= models.CharField(max_length=35)
    apellido=models.CharField(max_length=35)
    email=models.EmailField(max_length=40)
    asunto=models.CharField(max_length=150)
    mensaje=models.TextField()
    def __str__(self):
        return self.nombre
