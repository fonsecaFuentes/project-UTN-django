from django.contrib import admin
from .models import Pumps
from .models import MechanicalSeal
from .models import Packing
from motors.models import Motor
from bearings.models import PumpBearing


# Register your models here.
class MotorInLine(admin.TabularInline):
    model = Motor
    extra = 0


class BearingInLine(admin.TabularInline):
    model = PumpBearing
    extra = 0


@admin.register(Pumps)
class PumpAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'tag', 'brand', 'model', 'types', 'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'tag', 'brand', 'model', 'kind_of_pump',
        'description', 'image', 'upper_case_name',
    ]

    ordering = ['tag']
    list_filter = ('tag', 'types')
    search_fields = ('tag', 'types')

    inlines = [MotorInLine, BearingInLine]

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s %s %s" % (obj.tag, obj.brand, obj.model)).upper()


@admin.register(MechanicalSeal)
class MechanicalSealAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'pump', 'brand', 'types',
                    'material', 'extention',
                    'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'brand', 'extention', 'kind_of_mechanicalseal',
        'kind_of_material', 'description',
        'image', 'upper_case_name',
    ]

    ordering = ['extention']
    list_filter = ('extention', 'types')
    search_fields = ('extention', 'types', 'pump')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.brand, obj.extention)).upper()


@admin.register(Packing)
class PackingSealAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'pump', 'material', 'extention',
                    'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'pump', 'kind_of_material', 'extention',
        'description', 'image', 'upper_case_name'
    ]

    ordering = ['extention']
    list_filter = ('extention',)
    search_fields = ('extention', 'pump')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.extention, obj.pump.tag)).upper()
