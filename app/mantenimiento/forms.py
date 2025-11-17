from django import forms
from datetime import date
from .models import OrdenDeTrabajo

class OrdenDeTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenDeTrabajo
        fields = ['titulo', 'fecha', 'descripcion_falla', 'prioridad']
        widgets = {
           'fecha': forms.DateInput(
               attrs={'type': 'date', 'class': 'input'}
            )
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha != date.today():
            raise forms.ValidationError("La fecha debe ser la actual.")
        return fecha

    def clean_descripcion_falla(self):
        texto = self.cleaned_data['descripcion_falla']
        if len(texto) < 20:
            raise forms.ValidationError("La descripción debe tener al menos 20 caracteres.")
        return texto

    def clean(self):
        cleaned_data = super().clean()
        prioridad = cleaned_data.get('prioridad')
        descripcion = cleaned_data.get('descripcion_falla', '')
        if prioridad == 'Alta' and not any(p in descripcion.lower() for p in ['detenido', 'bloqueado', 'fuego']):
            raise forms.ValidationError("Para prioridad Alta, debe incluir una palabra clave de urgencia.")
        return cleaned_data

class AsignarOrdenForm(forms.ModelForm):
    class Meta:
        model = OrdenDeTrabajo
        fields = ['operario_asignado', 'fecha_cierre_real']
        widgets = {
            'fecha_cierre_real': forms.DateInput(attrs={'type': 'date', 'class': 'input'})
        }
