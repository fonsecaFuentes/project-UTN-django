from django.contrib import admin
from .models import Coupling


# Register your models here.
@admin.register(Coupling)
class CouplingAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'pump', 'motor', 'brand', 'types', 'series',
                    'description', 'image'
                ]
            }
        ),
        (
            'Medida eje bomba', {
                'fields': [
                    'pump_shaft_measurement',
                ]
            }
        ),
        (
            'Medidas de chaveta Bomba', {
                'fields': [
                    'high_pump_key_size', 'width_pump_key_size',
                    'long_pump_key_size'
                ],
            }
        ),
        (
            'Medida eje motor', {
                'fields': [
                    'engine_shaft_measurement',
                ]
            }
        ),
        (
            'Medidas de chaveta Motor', {
                'fields': [
                    'high_motor_key_size', 'width_motor_key_size',
                    'long_motor_key_size'
                ],
            }
        ),
    ]

    list_display = [
        'series', 'coupling_type', 'engine_keyway', 'pump_keyway',
        'image', 'upper_case_name',
    ]

    ordering = ['series']

    list_filter = (
        'series', 'pump_shaft_measurement', 'engine_shaft_measurement', 'types'
    )

    search_fields = (
        'series', 'pump_shaft_measurement', 'engine_shaft_measurement', 'types'
    )

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return (
            "%s %s - Bomba %s" % (obj.series, obj.motor.quiver, obj.pump.tag,)
        ).upper()

    @admin.display(description='Engine Keyway')
    def engine_keyway(self, obj):
        return f"{obj.width_motor_key_size} x {obj.high_motor_key_size} x\
             {obj.long_motor_key_size}"

    @admin.display(description='Pump Keyway')
    def pump_keyway(self, obj):
        width = obj.width_pump_key_size
        height = obj.high_pump_key_size
        length = obj.long_pump_key_size

        return f"{width} x {height} x {length}"
