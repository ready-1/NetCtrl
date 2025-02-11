from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django import forms
import os

# Import models at module level
from .models import Switch


class SwitchAdminForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="CLI credentials (encrypted at rest)",
        required=False
    )

    class Meta:
        model = Switch
        fields = '__all__'
        exclude = ['encrypted_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        
        # Set initial values for existing instances
        if instance:
            self.fields['password'].initial = instance.password
        # Set default values for new instances
        else:
            self.fields['username'].initial = os.getenv('SWITCH_DEFAULT_USERNAME', 'admin')
            self.fields['password'].initial = os.getenv('SWITCH_DEFAULT_PASSWORD', 'FuseFuse123!')
            self.fields['aaa_config'].initial = 'aaa authorization tracing enabled'
            self.fields['cli_timeout'].initial = 30
            self.fields['igmp_snooping_enabled'].initial = True
            # cert_expiry is optional, so no default needed

        self.fields['aaa_config'].help_text = format_html(
            'Follow <a href="{}">AAA config guidelines</a>',
            reverse(
                "view_cli_manual",
                args=["aaa_authorization_tracing_enabled.md"],
            ),
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('password'):
            instance.password = self.cleaned_data['password']
        if commit:
            instance.save()
        return instance


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    form = SwitchAdminForm
    list_display = (
        "name",
        "in_band_ip",
        "out_band_ip",
        "cert_expiry",
        "cli_timeout",
        "igmp_snooping_status",
    )
    list_editable = ("cli_timeout",)
    readonly_fields = ("last_cert_renewal",)

    fieldsets = (
        (
            "Network Configuration",
            {"fields": ("name", ("in_band_ip", "out_band_ip"), "username", "password")},
        ),
        (
            "Security Settings",
            {
                "fields": (
                    "aaa_config",
                    "cert_expiry",
                    "last_cert_renewal",
                    "igmp_snooping_enabled",
                )
            },
        ),
        ("CLI Parameters", {"fields": ("cli_timeout",)}),
    )

    def igmp_snooping_status(self, obj):
        return "Enabled" if obj.igmp_snooping_enabled else "Disabled"

    igmp_snooping_status.short_description = "IGMP Snooping"
