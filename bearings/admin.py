from django.contrib import admin
from .models import Bearing
from .models import PumpBearing
from .models import MotorBearing


# Register your models here.
class PumpBearingInLine(admin.TabularInline):
    model = PumpBearing
    extra = 0


class MotorBearingInLine(admin.TabularInline):
    model = MotorBearing
    extra = 0


@admin.register(Bearing)
class BearingAdmin(admin.ModelAdmin):
    inlines = [PumpBearingInLine, MotorBearingInLine]

    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'side', 'types', 'brand', 'number_reference',
                    'inner_diameter', 'outer_diameter',
                    'broad', 'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'number_reference', 'side_equipment', 'brand', 'kind_of_bearing',
        'inner_diameter', 'outer_diameter', 'broad',
        'description', 'image', 'upper_case_name',
    ]

    ordering = ['number_reference']
    list_filter = ('number_reference', 'types')
    search_fields = ('number_reference', 'types')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s" % (obj.number_reference)).upper()


@admin.register(PumpBearing)
class PumpBearingAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'pump', 'bearing'
                ]
            }
        )
    ]

    list_display = [
        'pump', 'upper_case_name'
    ]

    ordering = ['pump']
    list_filter = ('pump', 'bearing')
    search_fields = ('pump', 'bearing')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s - %s - %s - %s" % (
            obj.bearing.number_reference,
            obj.bearing.brand,
            obj.bearing.side,
            obj.bearing.types
        )).upper()


@admin.register(MotorBearing)
class MotorBearingAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'motor', 'bearing'
                ]
            }
        )
    ]

    list_display = [
        'motor', 'upper_case_name'
    ]

    ordering = ['motor']
    list_filter = ('motor', 'bearing')
    search_fields = ('motor', 'bearing')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s - %s - %s - %s" % (
            obj.bearing.number_reference,
            obj.bearing.brand,
            obj.bearing.side,
            obj.bearing.types
        )).upper()
