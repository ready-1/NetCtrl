from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Netgear 
from .forms import NetgearForm


def devices(request):
    devs = Netgear.objects.all()
    
    # check if devices are online
    # for dev in devs:
    #     dev.
            

    return render(request, "devices/devices.html", { 'devices' : devs })

def device(request, short_name):
    dev = Netgear.objects.get(short_name=short_name)
    return render(request, "devices/device.html", { 'device' : dev })

def edit(request, short_name):
    device = Netgear.objects.get(short_name=short_name)
    if request.method == "POST":
        form = NetgearForm(request.POST)
        if form.is_valid():

            device.save()
            return HttpResponseRedirect("/")
    else:
        form = NetgearForm(
            initial={"title": device.short_name, }
        )
    return render(request, "devices/edit.html", {"device": device, "form": form})


def delete(request, short_name):
    device = Netgear.objects.get(short_name=short_name)
    if request.method == "POST":
        device.delete()
        return HttpResponseRedirect(reverse("devices:devices"))

    return render(request, "devices/delete.html", {"device": device})

def create(request):
    if request.method == "POST":
        form = NetgearForm(request.POST)
        if form.is_valid():
            device = Netgear()
            device.short_name = form.cleaned_data["short_name"]
            device.in_band_ip = form.cleaned_data["in_band_ip"]
            device.out_band_ip = form.cleaned_data["out_band_ip"]
            device.username = form.cleaned_data["username"]
            device.password = form.cleaned_data["password"]
            device.save()
            return HttpResponseRedirect("/devices/")
    else:
        form = NetgearForm(initial={"title": "Device Short Name", })
    return render(request, "devices/create.html", {"form": form})