from django import forms
from contato.models import Contato
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(required=True, min_length=3)
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField(required=True, min_length=3)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Esse email ja esta cadastrado!',
                                code='invalid')
            )
        return email
