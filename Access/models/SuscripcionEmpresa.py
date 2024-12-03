import os
import uuid

from django.db import models

from Access.models import Empresa

def unique_image_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{extension}"
    return os.path.join('suscripcion/', unique_filename)


class SuscripcionEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='suscripciones')
    nombre = models.CharField(max_length=255)
    monto_total_puntos = models.DecimalField(max_digits=10, decimal_places=2)  # Límite de puntos
    frecuencia = models.CharField(max_length=50, choices=[('S', 'Semanal'), ('M', 'Mensual'), ('A', 'Anual')])
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to=unique_image_path, null=True, blank=True)

    def unique_image_path(instance, filename):
        extension = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4()}{extension}"
        return os.path.join('suscripcion/', unique_filename)

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"
