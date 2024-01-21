from django.db import models
from django.utils.html import format_html


# Create your models here.
class Pumps(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)

    centrifuge = 'Centrífuga'
    gears = 'Engranajes'
    pneumatics = 'Neumática'

    pump_type = (
        (centrifuge, 'Centrífuga'),
        (gears, 'Engranajes'),
        (pneumatics, 'Neumática'),
    )
    types = models.CharField(
        max_length=50, choices=pump_type, default='Centrífuga'
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        default='bombas/default/pump.png',
        upload_to='bombas',
        verbose_name='Imagen de bomba',
        blank=True
    )

    def kind_of_pump(self):
        if self.types == 'Centrífuga':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.types
            )
        elif self.types == 'Engranajes':
            return format_html(
                '<span style="color: #099;">{}</span>', self.types
            )
        elif self.types == 'Neumática':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.types
            )

    class Meta:
        verbose_name = "Bomba"
        verbose_name_plural = "Bombas"

    def __str__(self):
        return f"{self.tag} - {self.brand} - {self.model}"


class MechanicalSeal(models.Model):
    pump = models.ForeignKey(Pumps, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=True)

    conical_spring_seals = 'Sellos de Resorte Cónico'
    metal_bellows_seals = 'Sellos de Fuelle Metálico'
    cartridge_seals = 'Sellos de Cartucho'

    mechanicalseal_type = (
        (conical_spring_seals, 'Sellos de Resorte Cónico'),
        (metal_bellows_seals, 'Sellos de Fuelle Metálico'),
        (cartridge_seals, 'Sellos de Cartucho'),
    )

    types = models.CharField(
        max_length=50,
        choices=mechanicalseal_type,
        default='Sellos de Resorte Cónico'
    )

    silicon_carbide_SiC = 'Carburo de Silicio (SiC)'
    graphite = 'Grafito'
    nickel_chromium_alloys = 'Aleaciones de Níquel-Cromo'
    stainless_steel = 'Acero Inoxidable'
    ceramic = 'Cerámica'

    material_types = (
        (silicon_carbide_SiC, 'Carburo de Silicio (SiC)'),
        (graphite, 'Grafito'),
        (nickel_chromium_alloys, 'Aleaciones de Níquel-Cromo'),
        (stainless_steel, 'Acero Inoxidable'),
        (ceramic, 'Cerámica'),
    )

    material = models.CharField(
        max_length=50,
        choices=material_types,
        default='Carburo de Silicio (SiC)'
    )

    # medidas
    extention = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='sellos_mecanicos/default/mechanical_seal.png',
        upload_to='sellos_mecanicos',
        verbose_name='Imagen de sello_mecanico',
        blank=True
    )

    def kind_of_mechanicalseal(self):
        if self.types == 'Sellos de Resorte Cónico':
            return format_html(
                '<span style="color: #f00;">{}</span>', self.types
            )
        elif self.types == 'Sellos de Fuelle Metálico':
            return format_html(
                '<span style="color: #099;">{}</span>', self.types
            )
        elif self.types == 'Sellos de Cartucho':
            return format_html(
                '<span style="color: #f0f;">{}</span>', self.types
            )

    def kind_of_material(self):
        if self.material == 'Carburo de Silicio (SiC)':
            return format_html(
                '<span style="color: #D435BC;">{}</span>', self.types
            )
        elif self.material == 'Grafito':
            return format_html(
                '<span style="color: #A135D4;">{}</span>', self.types
            )
        elif self.material == 'Aleaciones de Níquel-Cromo':
            return format_html(
                '<span style="color: #FF5733;">{}</span>', self.types
            )
        elif self.material == 'Acero Inoxidable':
            return format_html(
                '<span style="color: #33F3FF;">{}</span>', self.types
            )
        elif self.material == 'Cerámica':
            return format_html(
                '<span style="color: #DAF7A6;">{}</span>', self.types
            )

    class Meta:
        verbose_name = 'Sello Mecánico'
        verbose_name_plural = 'Sellos Mecánicos'

    def __str__(self):
        return f"Sello - {self.types} - {self.extention}\
             de Bomba {self.pump.tag}"


class Packing(models.Model):
    pump = models.ForeignKey(Pumps, on_delete=models.CASCADE)

    asbestos = 'Asbesto'
    teflon = 'Teflon'
    graphite = 'Grafito'

    material_types = (
        (asbestos, 'Asbesto'),
        (teflon, 'Teflon'),
        (graphite, 'Grafito'),
    )

    material = models.CharField(
        max_length=50,
        choices=material_types,
        default='Asbesto'
    )

    # medidas
    extention = models.PositiveIntegerField(
        blank=True, null=True, help_text="millimeters (mm)"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='empaquetaduras/default/packing.png',
        upload_to='empaquetaduras',
        verbose_name='Imagen de empaquetadura',
        blank=True
    )

    def kind_of_material(self):
        if self.material == 'Asbesto':
            return format_html(
                '<span style="color: #D435BC;">{}</span>', self.types
            )
        elif self.material == 'Teflon':
            return format_html(
                '<span style="color: #A135D4;">{}</span>', self.types
            )
        elif self.material == 'Grafito':
            return format_html(
                '<span style="color: #FF5733;">{}</span>', self.types
            )

    class Meta:
        verbose_name = 'Empaquetadura'
        verbose_name_plural = 'Empaquetaduras'

    def __str__(self):
        return f"Empaquetadura - {self.material} - {self.extention}\
             de Bomba {self.pump.tag}"
