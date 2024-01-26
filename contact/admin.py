from django.contrib import admin
from .models import Consult
from .models import Response


# Register your models here.
class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0


@admin.register(Consult)
class ConsultInline(admin.ModelAdmin):
    inlines = [ResponseInline]
    list_display = [
        'response_statuses', 'name', 'description',
        'email', 'telephone', 'date'
        ]
    list_filter = ['status_response', 'date']
