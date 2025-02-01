from django import forms
from .models import Switch


class SwitchForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Switch
        fields = ["name", "ip_address", "username", "password"]


class TestForm(forms.Form):
    required_field = forms.CharField(required=True)
    optional_field = forms.CharField(required=False)
