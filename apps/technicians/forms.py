from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'