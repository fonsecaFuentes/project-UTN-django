# from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import Consult


class ConsultForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consult
        fields = [
            'name',
            'description',
            'email',
            'telephone',
        ]

    def send_email(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        email = self.cleaned_data['email']
        telephone = self.cleaned_data['telephone']

        print("enviando datos")
        print(name, description, email, telephone)
        # # Lógica envio de email
