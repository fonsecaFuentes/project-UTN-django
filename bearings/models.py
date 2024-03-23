from django.db import models
from pumps.models import Pumps
from motors.models import Motor
from django.utils.html import format_html


# Create your models here.
class Bearing(models.Model):
    front_bearing = 'rodamiento delantero'
    rear_bearing = 'rodamiento trasero'

    side_of_object = (
        (front_bearing, 'rodamiento delantero'),
        (rear_bearing, 'rodamiento trasero'),
    )

    side = models.CharField(
        max_length=50, choices=side_of_object, default='rodamiento delantero'
    )

    deep_groove_ball_bearing = 'Rodamiento de bolas rígido'
    cylindrical_roller_bearing = 'Rodamiento de rodillos cilíndricos'
    angular_contact_ball_bearing = 'Rodamiento de contacto angular de bolas'

    bearing_type = (
        (deep_groove_ball_bearing, 'Rodamiento de bolas rígido'),
        (cylindrical_roller_bearing, 'Rodamiento de rodillos cilíndricos'),
        (
            angular_contact_ball_bearing,
            'Rodamiento de contacto angular de bolas'
        ),
    )

    types = models.CharField(
        max_length=50, choices=bearing_type,
        default='Rodamiento de bolas rígido'
    )
    number_reference = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)

    # Medidas de los rodamientos en mm
    # Medida interna
    inner_diameter = models.PositiveIntegerField(
        blank=True, null=True, help_text="milímetros (mm)"
    )
    # Medida externa
    outer_diameter = models.PositiveIntegerField(
        blank=True, null=True, help_text="milímetros (mm)"
    )
    # Ancho
    broad = models.PositiveIntegerField(
        blank=True, null=True, help_text="milímetros (mm)"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='rodamientos/default/bearing.png',
        upload_to='rodamientos',
        verbose_name='Imagen de rodamiento',
        blank=True
    )

    def kind_of_bearing(self):
        if self.types == 'Rodamiento de bolas rígido':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.types
            )
        elif self.types == 'Rodamiento de rodillos cilíndricos':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.types
            )
        elif self.types == 'Rodamiento de contacto angular de bolas':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.types
            )

    def side_equipment(self):
        if self.side == 'rodamiento delantero':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.side
            )
        elif self.side == 'rodamiento trasero':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.side
            )

    class Meta:
        verbose_name = 'Rodamiento'
        verbose_name_plural = 'Rodamientos'

    def __str__(self):
        return f"Rodamiento - {self.number_reference}"


class PumpBearing(models.Model):
    pump = models.ForeignKey(
         Pumps, on_delete=models.CASCADE,
         null=True, blank=True, related_name='bearings'
    )
    bearing = models.ForeignKey(
        Bearing, on_delete=models.CASCADE, related_name='pump_bearings'
    )

    def __str__(self):
        return f"{self.pump} - {self.bearing} - {self.bearing.side}"


class MotorBearing(models.Model):
    motor = models.ForeignKey(
         Motor, on_delete=models.CASCADE,
         null=True, blank=True, related_name='bearings'
    )
    bearing = models.ForeignKey(
        Bearing, on_delete=models.CASCADE, related_name='motor_bearings'
    )

    def __str__(self):
        return f"{self.motor} - {self.bearing} - {self.bearing.side}"
