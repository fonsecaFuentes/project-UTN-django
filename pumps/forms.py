from django import forms
from .models import Pumps
from .models import MechanicalSeal


class ConsultForm(forms.ModelForm):
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
            'brand': 'Marca',
            'model': 'Modelo',
            'types': 'Tipo de Bomba',
            'description': 'Descripción',
            'image': 'Imagen de la Bomba',
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