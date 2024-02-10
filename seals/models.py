from django.db import models
from pumps.models import Pumps
from motors.models import Motor
from django.utils.html import format_html


# Create your models here.
class Seal(models.Model):
    front_seal = 'reten delantero'
    rear_seal = 'reten trasero'

    side_of_object = (
        (front_seal, 'reten delantero'),
        (rear_seal, 'reten trasero')
    )

    side = models.CharField(
        max_length=50, choices=side_of_object, default='reten delantero'
    )

    single_lip_seal = 'Reten de labio simple'
    double_lip_seal = 'Reten de labio doble'

    seal_type = (
        (single_lip_seal, 'Reten de labio simple'),
        (double_lip_seal, 'Reten de labio doble'),
    )

    types = models.CharField(
        max_length=50, choices=seal_type, default='Reten de labio simple'
    )

    # Medidas de los retenes en mm
    # Medida interna
    inner_diameter = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )
    # Medida externa
    outer_diameter = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )
    # Ancho
    broad = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )
    number_reference = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='retenes/default/seals.png',
        upload_to='retenes',
        verbose_name='Imagen de reten',
        blank=True
    )

    def kind_of_seal(self):
        if self.types == 'Reten de labio simple':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.types
            )
        elif self.types == 'Reten de labio doble':
            return format_html(
                '<span style="color: #099;">{}</span>', self.types
            )

    def side_equipment(self):
        if self.side == 'reten delantero':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.side
            )
        elif self.side == 'reten trasero':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.side
            )

    class Meta:
        verbose_name = 'Reten'
        verbose_name_plural = 'Retenes'

    def __str__(self):
        return f"Reten - {self.inner_diameter} x {self.outer_diameter}\
             x {self.broad}"


class PumpSeal(models.Model):
    pump = models.ForeignKey(
         Pumps, on_delete=models.CASCADE,
         null=True, blank=True, related_name='seal'
    )
    seal = models.ForeignKey(
        Seal, on_delete=models.CASCADE, related_name='pump_seal'
    )

    def __str__(self):
        return f"{self.pump} - {self.seal}"


class MotorSeal(models.Model):
    motor = models.ForeignKey(
         Motor, on_delete=models.CASCADE,
         null=True, blank=True, related_name='seal'
    )
    seal = models.ForeignKey(
        Seal, on_delete=models.CASCADE, related_name='motor_seal'
    )

    def __str__(self):
        return f"{self.motor} - {self.seal}"
