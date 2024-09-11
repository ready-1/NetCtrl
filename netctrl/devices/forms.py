from django.forms import ModelForm
from .models import Netgear

class NetgearForm(ModelForm):
    class Meta:
        model = Netgear
        fields = '__all__'