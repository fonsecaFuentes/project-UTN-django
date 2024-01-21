from django.contrib import admin
from .models import Seal
from .models import PumpSeal
from .models import MotorSeal


# Register your models here.
class PumpSealInLine(admin.TabularInline):
    model = PumpSeal
    extra = 0


class MotorSealInLine(admin.TabularInline):
    model = MotorSeal
    extra = 0


@admin.register(Seal)
class SealAdmin(admin.ModelAdmin):
    inlines = [PumpSealInLine, MotorSealInLine]

    fieldsets = [
        (
            'Datos Generales', {
                'fields': [
                    'side', 'types', 'number_reference',
                    'inner_diameter', 'outer_diameter',
                    'broad', 'description', 'image'
                ]
            }
        )
    ]

    list_display = [
        'kind_of_seal', 'side_equipment', 'inner_diameter',
        'outer_diameter', 'broad', 'description',
        'image', 'upper_case_name', 'number_reference',
    ]

    ordering = ['number_reference']
    list_filter = ('number_reference', 'types')
    search_fields = ('number_reference', 'types')

    @admin.display(description='Datos')
    def upper_case_name(self, obj):
        return ("%s" % (obj.number_reference)).upper()


admin.site.register(PumpSeal)
admin.site.register(MotorSeal)
