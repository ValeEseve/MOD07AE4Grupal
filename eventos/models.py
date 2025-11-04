from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(blank=True)

    def __str__(self):
        return f"Evento {self.nombre}, fecha {self.fecha}, en ubicación {self.ubicacion}"

class Participante(models.Model):
    nombre = models.CharField()
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.nombre} - {self.email}"