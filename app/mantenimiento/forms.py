from django import forms
from .models import OrdenDeTrabajo

class OrdenDeTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenDeTrabajo
        fields = ['titulo', 'fecha', 'descripcion_falla', 'prioridad']

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
