from django.db import models

# Create your models here.
class Netgear(models.Model):
    short_name = models.CharField(max_length=100)
    in_band_ip = models.CharField(max_length=15)
    out_band_ip = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login_token = models.CharField(max_length=100, default="", blank=True)
    login_epoch_time = models.IntegerField(default=0, blank=True)
    
    # #  from /device_info
    # # "name": "<string>",
    # name = models.CharField(max_length=100)
    # # "serialNumber": "<string>",
    # serial_number = models.CharField(max_length=50)
    # # "macAddr": "<string>",
    # mac_addr = models.CharField(max_length=18)
    # # "model": "<string>",
    # model = models.CharField(max_length=50)
    # # "lanIpAddress": "<string>",
    # lan_ip_address = models.CharField(max_length=15)
    # # "swVer": "<string>",
    # sw_ver = models.CharField(max_length=50)
    # # "lastReboot": "<string>",
    # last_reboot = models.CharField(max_length=50)
    # # "numOfPorts": "<integer>",
    # num_of_ports = models.IntegerField()
    # #     "bootVersion": "<string>",

    def __str__(self):
        return self.short_name 