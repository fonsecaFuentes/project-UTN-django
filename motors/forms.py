from django import forms
from .models import Motor


class MotorForm(forms.ModelForm):

    class Meta:
        model = Motor
        fields = [
            'brand',
            'quiver',
            'hp',
            'rpm',
            'antiexplosive',
            'description',
            'image'
        ]
        labels = {
            'brand': 'Fabricante',
            'quiver': 'Carcasa',
            'hp': 'HP',
            'rpm': 'RPM',
            'antiexplosive': 'Antiexplosivo',
            'description': 'Descripción',
            'image': 'Imagen de Motor',
        }

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'quiver': forms.TextInput(attrs={'class': 'form-control'}),
            'hp': forms.NumberInput(attrs={'class': 'form-control'}),
            'rpm': forms.NumberInput(attrs={'class': 'form-control'}),
            'antiexplosive': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
