from django.db import models
from django.contrib.auth.models import User

class RegistroTrabajo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    horas_trabajadas = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField()
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.descripcion} - {self.usuario.username}'
