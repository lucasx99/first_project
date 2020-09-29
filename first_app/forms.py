from django import forms
from django.core import validators

from first_app.models import Topico,Webpage, Pessoa


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")


class FormName(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    texto = forms.CharField(widget=forms.Textarea, validators=[check_for_z])


class ModelForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = "__all__"

class FiveModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
