from django.db import models
from pumps.models import Pumps
from motors.models import Motor
from django.utils.html import format_html


# Create your models here.
class Coupling(models.Model):
    pump = models.ForeignKey(Pumps, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=True)

    semi_elastic = 'Semi-Elástico'
    elastic = 'Elástico'

    coupling_type = (
        (semi_elastic, 'Semi-Elástico'),
        (elastic, 'Elástico'),
    )

    types = models.CharField(
        max_length=100, choices=coupling_type, default='Elástico', blank=True
    )
    series = models.CharField(max_length=100, blank=True)
    motor_side_measure = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )

    # medidas mecanizado eje del lado bomba y motor
    # medida bomba
    pump_shaft_measurement = models.PositiveIntegerField(
        blank=True, null=True, help_text="medida eje lado bomba (mm)"
    )
    # medida motor
    engine_shaft_measurement = models.PositiveIntegerField(
        blank=True, null=True, help_text="medida eje lado motor (mm)"
    )

    # medidas chaveta lado bomba
    # medida alto
    high_pump_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida alto (mm)"
    )
    # medida ancho
    width_pump_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida ancho (mm)"
    )
    # medida largo
    long_pump_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida largo (mm)"
    )

    # medidas chaveta lado motor
    # medida alto
    high_motor_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida alto (mm)"
    )
    # medida ancho
    width_motor_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida ancho (mm)"
    )
    # medida largo
    long_motor_key_size = models.PositiveIntegerField(
        blank=True, null=True, help_text="chaveta medida largo (mm)"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='acoples/default/mechanical_coupling.png',
        upload_to='acoples/',
        verbose_name='Imagen de acolple',
        blank=True
    )

    def coupling_type(self):
        if self.types == 'Elástico':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.types
            )
        elif self.types == 'Semi-Elástico':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.types
            )

    class Meta:
        verbose_name = 'Acople'
        verbose_name_plural = 'Acoples'

    def __str__(self):
        return f"Acolple - Motor {self.motor.quiver} - Bomba {self.pump.tag}"
