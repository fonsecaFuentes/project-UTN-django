from django import forms
from .models import Coupling


class CouplingForm(forms.ModelForm):

    class Meta:
        model = Coupling
        fields = [
            'brand',
            'types',
            'series',
            'pump_shaft_measurement',
            'engine_shaft_measurement',
            'high_pump_key_size',
            'width_pump_key_size',
            'long_pump_key_size',
            'high_motor_key_size',
            'width_motor_key_size',
            'long_motor_key_size',
            'description',
            'image'
        ]
        labels = {
            'brand': 'Fabricante',
            'types': 'Tipo de acople',
            'series': 'Serie',
            'pump_shaft_measurement': 'Medidas eje lado bomba (mm)',
            'engine_shaft_measurement': 'Medidas eje lado motor (mm)',
            'high_pump_key_size': 'Alto de chaveta (bomba) (mm)',
            'width_pump_key_size': 'Ancho de chaveta (bomba) (mm)',
            'long_pump_key_size': 'Largo de chaveta (bomba) (mm)',
            'high_motor_key_size': 'Alto de chaveta (motor) (mm)',
            'width_motor_key_size': 'Ancho de chaveta (motor) (mm)',
            'long_motor_key_size': 'Largo de chaveta (motor) (mm)',
            'description': 'Descripción',
            'image': 'Imagen de Acople',
        }

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'series': forms.TextInput(attrs={'class': 'form-control'}),
            'pump_shaft_measurement': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'engine_shaft_measurement': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'high_pump_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'width_pump_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'long_pump_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'high_motor_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'width_motor_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'long_motor_key_size': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
