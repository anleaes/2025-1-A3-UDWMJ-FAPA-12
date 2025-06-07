from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = '__all__'