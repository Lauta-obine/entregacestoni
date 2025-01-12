from django.db import models

 
# Create your models here.

class Tractor(models.Model):
    patente=models.CharField(max_length=8, unique=True)
    marca= models.CharField(max_length=20)
    ano= models.IntegerField(default="0000")

    def __str__(self):
        return self.patente
    
class Semi(models.Model):
    patente=models.CharField(max_length=8, unique=True)
    marca= models.CharField(max_length=20)
    tipo=models.CharField(max_length=20, default="")
    ano= models.IntegerField(default="0000")
    
    def __str__(self):
        return self.patente
            
class Chofer(models.Model):
   
    nombre= models.CharField(max_length=20)
    dni=models.IntegerField(unique=True)


    def __str__(self):
        return self.nombre