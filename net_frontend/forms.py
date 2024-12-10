from django import forms
from net_core.models import Switch
from django.core.validators import validate_ipv4_address

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = [
            'name', 'ip_address_in_band', 'ip_address_out_band',
            'mac_address', 'model', 'serial_number',
            'firmware_version', 'status', 'location',
            'port_count', 'asset_id', 'notes'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Switch Name'}),
            'ip_address_in_band': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'In-Band IP'}),
            'ip_address_out_band': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Out-of-Band IP'}),
            'mac_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MAC Address'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Switch Model'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial Number'}),
            'firmware_version': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firmware Version'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'port_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Port Count'}),
            'asset_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asset ID'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional Notes'}),
        }

    def clean_ip_address_in_band(self):
        ip = self.cleaned_data.get('ip_address_in_band')
        validate_ipv4_address(ip)
        return ip

    def clean_ip_address_out_band(self):
        ip = self.cleaned_data.get('ip_address_out_band')
        validate_ipv4_address(ip)
        return ip


