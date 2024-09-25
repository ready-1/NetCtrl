from django.forms import ModelForm
from .models import Netgear

class NetgearForm(ModelForm):
    class Meta:
        model = Netgear
        fields = ["short_name", 
                  "in_band_ip", 
                  "out_band_ip", 
                  "username", 
                  "password",]