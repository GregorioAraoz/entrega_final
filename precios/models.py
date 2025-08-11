from django.db import models

# Create your models here.
class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - $ {self.precio} / {self.unidad}"