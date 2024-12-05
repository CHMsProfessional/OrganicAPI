import os
import uuid

from django.contrib.auth.models import User
from django.db import models

from Access.models import Usuarios


def unique_image_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{extension}"
    return os.path.join('empresa/', unique_filename)

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    propietario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='empresas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to=unique_image_path, null=True, blank=True)

    def unique_image_path(instance, filename):
        extension = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4()}{extension}"
        return os.path.join('empresa/', unique_filename)

    def __str__(self):
        return self.nombre
