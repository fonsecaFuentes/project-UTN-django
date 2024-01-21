from django.contrib import admin
from .models import Motor
from bearings.models import MotorBearing


# Register your models here.
class BearingInLine(admin.TabularInline):
    model = MotorBearing
    extra = 0


@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'pump', 'brand', 'hp',
                    'rpm', 'quiver', 'antiexplosive',
                    'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'quiver', 'hp', 'rpm',
        'motor_antiexplosive',
        'description', 'image', 'upper_case_name',
    ]

    ordering = ['quiver']
    list_filter = ('quiver', 'hp', 'rpm', 'antiexplosive')
    search_fields = ('quiver', 'hp', 'rpm', 'antiexplosive')

    inlines = [BearingInLine]

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return (
            "%s %s - Bomba %s" % (obj.brand, obj.quiver, obj.pump.tag,)
        ).upper()
