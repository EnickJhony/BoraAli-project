from django import forms
from .models import Trilha

class TrilhaForm(forms.ModelForm):
    class Meta:
        model = Trilha
        fields = ('nome_trilha', 'descricao', 'localizacao', 'duracao', 'nivel', 'curiosidades', 'data_criacao')

        widgets = {
            'nome_trilha': forms.TextInput(attrs={'class':'form-control','autofocus':''}),
        }