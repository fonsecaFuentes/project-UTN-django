from django.db import models
from pumps.models import Pumps
from django.utils.html import format_html


# Create your models here.
class Motor(models.Model):
    pump = models.ForeignKey(Pumps, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=True)
    hp = models.PositiveIntegerField(
        blank=True, null=True, help_text="HP"
    )
    rpm = models.PositiveIntegerField(
         blank=True, null=True, help_text="RPM"
    )
    quiver = models.CharField(max_length=100, blank=True)
    antiexplosive = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(
        default='motores/default/electric_motor.png',
        upload_to='motores',
        verbose_name='Imagen de motor',
        blank=True
    )

    def motor_antiexplosive(self):
        if self.antiexplosive:
            return format_html(
                '<span style="color: #f00;">{}</span>', self.antiexplosive
            )
        else:
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.antiexplosive
            )

    class Meta:
        verbose_name = "Motor"
        verbose_name_plural = "Motores"

    def __str__(self):
        return f"Motor {self.quiver} de Bomba {self.pump.tag}"
