from django.db import models

class Animal(models.Model):
    especie = models.CharField(max_length=50)
    alimentacion = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.especie} - {self.alimentacion}"

#Para pasar un modelo a la base de datos, se debe ejecutar el comando:
    # python manage.py makemigrations
    
    #Con python manage.py migrate, se crea la tabla en la base de datos
    
    #Con python manage.py shell, se puede interactuar con la base de datos
    
    #Con exit() se sale del shell
    
    