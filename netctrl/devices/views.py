from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Netgear
from .forms import NetgearForm

def devices(request):
    devs = Netgear.objects.all()
    return render(request, "devices/devices.html", { 'devices' : devs })

def device(request, short_name):
    dev = Netgear.objects.get(short_name=short_name)
    return render(request, "devices/device.html", { 'device' : dev })

def create(request):

    return render(request, "devices/create.html")
