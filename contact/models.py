from django.db import models
from django.utils.html import format_html
from datetime import datetime


# Create your models here.
class Consult(models.Model):
    answered = 'Contestada'
    not_answered = 'No contestada'
    in_progress = 'En curso'

    response_status = (
        (answered, 'Contestada'),
        (not_answered, 'No contestada'),
        (in_progress, 'En curso'),
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    status_response = models.CharField(
        max_length=20, choices=response_status, default='No contestada'
    )
    telephone = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(
        default=datetime.now, blank=True, null=True, editable=True
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def response_statuses(self):
        if self.status_response == 'Contestada':
            return format_html(
                '<span style="background-color:#0a0; color: #fff;\
                 padding:5px;">{}</span>',
                self.status_response
            )
        elif self.status_response == 'No contestada':
            return format_html(
                '<span style="background-color:#a00; color: #fff;\
                 padding:5px;">{}</span>',
                self.status_response
            )
        elif self.status_response == 'En curso':
            return format_html(
                '<span style="background-color:#FOB203;color: #000;\
                 padding:5px;">{}</span>',
                self.status_response
            )


class Response(models.Model):
    consult = models.ForeignKey(
        Consult, on_delete=models.CASCADE, blank=True, null=True
    )
    response = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.now, blank=True, editable=True)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def create_message(self):
        change_status = Consult.objects.get(id=self.consult.id)
        change_status.status_response = 'Contestada'
        change_status.save()
        # Lógica de envio de email

    def save(self, *args, **kwargs):
        self.create_message()
        force_update = False
        if self.id:
            force_update = True
        super(Response, self).save(force_update=force_update)
