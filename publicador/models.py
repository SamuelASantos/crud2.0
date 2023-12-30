from django.db import models

# Create your models here.
class Publicador(models.Model):
    name = models.CharField(max_length=100)
    baptism = models.DateField()

    def __str__(self):
        return self.name