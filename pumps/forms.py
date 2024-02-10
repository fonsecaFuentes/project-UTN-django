from django import forms
from .models import Pumps
from .models import MechanicalSeal


class PumpsForm(forms.ModelForm):
    class Meta:
        model = Pumps
        fields = [
            'tag',
            'brand',
            'model',
            'types',
            'description',
            'image',
        ]
        labels = {
            'tag': 'TAG',
            'brand': 'Fabricante',
            'model': 'Modelo',
            'types': 'Tipo de Bomba',
            'description': 'Descripción',
            'image': 'Imagen de Bomba',
        }

        widgets = {
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class MechanicalSealForm(forms.ModelForm):
    class Meta:
        model = MechanicalSeal
        fields = [
            'brand',
            'types',
            'material',
            'extention',
            'description',
            'image',
        ]
        labels = {
            'brand': 'Marca',
            'types': 'Tipo de Sello',
            'material': 'Meteriales de contacto',
            'extention': 'Medida',
            'description': 'Descripción',
            'image': 'Imagen del Sello',
        }
