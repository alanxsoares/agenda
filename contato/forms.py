from django import forms
from contato.models import Contato
from django.core.exceptions import ValidationError


class ContatoModelForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'categoria', 'img']

    def clean(self):

        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        sobrenome = cleaned_data.get('sobrenome')

        if nome == sobrenome:
            self.add_error(
                'sobrenome',
                ValidationError('Sobrenome e nome devem ser diferentes'))

        return super().clean()
