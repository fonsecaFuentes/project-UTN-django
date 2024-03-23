from django import forms
from .models import Bearing


class BearingForm(forms.ModelForm):

    class Meta:
        model = Bearing
        fields = [
            'side',
            'types',
            'number_reference',
            'brand',
            'inner_diameter',
            'outer_diameter',
            'broad',
            'description',
            'image'
        ]
        labels = {
            'side': 'Lado',
            'types': 'Tipo de Rodamiento',
            'number_reference': 'Número de Referencia',
            'brand': 'Fabricante',
            'inner_diameter': 'Medida Diámetro Interno',
            'outer_diameter': 'Medida Diámetro Externo',
            'broad': 'Medida Ancho',
            'description': 'Descripción',
            'image': 'Imagen de Rodamienmto',
        }

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'side': forms.Select(attrs={'class': 'form-control'}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'number_reference': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'inner_diameter': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'outer_diameter': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'broad': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class BearingBaseForm(forms.ModelForm):
    class Meta:
        model = Bearing
        fields = ['description', 'image']

        labels = {
            'description': 'Descripción',
            'image': 'Imagen de Rodamienmto',
        }

        widgets = {
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
