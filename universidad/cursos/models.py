from django.db import models

class Curso(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 6)
    nombre = models.CharField(max_length = 50) 
    nota =  models.PositiveSmallIntegerField() #Campo pequeño y positivo
    
    """ Metodo para ver los objetos """
    def __str__(self):
        text = f"{self.nombre}"
        return text
