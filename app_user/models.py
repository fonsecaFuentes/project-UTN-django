from django.db import models
from django.contrib.auth.models import User
from pumps.models import Pumps
from motors.models import Motor
from couplings.models import Coupling


# Create your models here.
class DataUser(models.Model):
    user = models.ForeignKey(
        User, blank=False, null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='usuarios/',
        default='usuarios/default/user.png',
        blank=True,
        null=True,
        verbose_name='Imagen de perfil'
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        if self.user.first_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.email


class Tasks(models.Model):
    user = models.ForeignKey(
        User, blank=False, null=True, on_delete=models.CASCADE
    )
    pump = models.ForeignKey(
        Pumps, blank=False, null=True, on_delete=models.CASCADE
    )
    engine = models.ForeignKey(
        Motor, blank=False, null=True, on_delete=models.CASCADE
    )
    coupling = models.ForeignKey(
        Coupling, blank=False, null=True, on_delete=models.CASCADE
    )
    types = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    urgent = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(
        default='tareas/default/tasks.png',
        upload_to='tareas',
        verbose_name='Imagen tarea',
        blank=True
    )
    image = models.ImageField(
        default='tareas/default/tasks.png',
        upload_to='tareas',
        verbose_name='Imagen tarea',
        blank=True
    )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return f"Tarea: {self.types}, {self.urgent}, {self.date}"


class Observations(models.Model):
    user = models.ForeignKey(
        User, blank=False, null=True, on_delete=models.CASCADE
    )
    pump = models.ForeignKey(
        Pumps, blank=False, null=True, on_delete=models.CASCADE
    )
    engine = models.ForeignKey(
        Motor, blank=False, null=True, on_delete=models.CASCADE
    )
    coupling = models.ForeignKey(
        Coupling, blank=False, null=True, on_delete=models.CASCADE
    )
    date = models.DateField()
    description = models.TextField(blank=True)
    image = models.ImageField(
        default='observaciones/default/observations.png',
        upload_to='observaciones',
        verbose_name='Imagen',
        blank=True
    )
    image = models.ImageField(
        default='observaciones/default/observations.png',
        upload_to='observaciones',
        verbose_name='Imagen',
        blank=True
    )

    class Meta:
        verbose_name = "Observacion"
        verbose_name_plural = "Observaciones"

    def __str__(self):
        return f"{self.description}, {self.date}"
