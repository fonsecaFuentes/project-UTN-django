from django import forms
from captcha.fields import CaptchaField
from .models import Consult


class ConsultForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consult
        fields = [
            'name',
            'description',
            'email',
            'telephone',
        ]
        labels = {
            'name': 'Nombre',
            'description': 'Comentario',
            'email': 'Email',
            'telephone': 'Telefono',
        }
        help_texts = {
            'telephone': 'Ingrese el número sin guiones ni espacios.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def send_email(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        email = self.cleaned_data['email']
        telephone = self.cleaned_data['telephone']

        print("enviando datos")
        print(name, description, email, telephone)
        # # Lógica envio de email
