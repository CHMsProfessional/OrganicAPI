from django.db import models

from Access.models import Usuarios


class MetodoPago(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name="metodos_pago")
    nombre_titular = models.CharField(max_length=100)  # Nombre del titular de la tarjeta
    numero_tarjeta = models.CharField(max_length=16)  # Número de tarjeta (enmascarado por seguridad)
    fecha_expiracion = models.CharField(max_length=5)  # Fecha de expiración (MM/AA)
    cvv = models.CharField(max_length=3)  # CVV de la tarjeta
    es_visa = models.BooleanField(default=True)  # Confirmación de que es tarjeta Visa
    creado_en = models.DateTimeField(auto_now_add=True)

    def verify_validez_tarjeta(self):

        if len(self.numero_tarjeta) != 16 or not self.numero_tarjeta.isdigit():
            return False, 'El número de tarjeta debe tener 16 dígitos.'

        if not self.numero_tarjeta.startswith('4'):
            return False, 'Solo se aceptan tarjetas Visa.'

        if len(self.fecha_expiracion) != 5 or '/' not in self.fecha_expiracion:
            return False, 'La fecha de expiración debe tener el formato MM/AA.'
        mes, anio = self.fecha_expiracion.split('/')
        if not (mes.isdigit() and anio.isdigit()):
            return False, 'La fecha de expiración debe tener el formato MM/AA.'
        if int(mes) < 1 or int(mes) > 12:
            return False, 'El mes de expiración debe estar entre 1 y 12.'

        if len(self.cvv) != 3 or not self.cvv.isdigit():
            return False, 'El CVV debe tener 3 dígitos.'

        return True

    def __str__(self):
        return f"{self.nombre_titular} - **** **** **** {self.numero_tarjeta[-4:]}"
