import os, sys
import json
import requests
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

    # #  from /self_info
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

    def __init__(self, *args, **kwargs):
        super(Netgear, self).__init__(*args, **kwargs)
        self.alive = self.is_alive()

    def make_url(self):
        return "https://" + self.out_band_ip + ":8443/api/v1/"

    def is_alive(self, in_band = False):
        # in_band = True ping the in_band_ip 
        # else ping the out_band_ip
        #  count = 1
        #  wait = 2


        param = '-n' if os.sys.platform.lower()=='win32' else '-c'
        hostname = self.in_band_ip if in_band else self.out_band_ip
        response = os.system(f"ping {param} 1 -W 2 {hostname}")

        #and then check the response...
        if response == 0:
            self.alive = True
            return True
        else:
            self.alive = False
            return False


    def login_to_switch(self):
        url = self.make_url() + "login"
        payload = json.dumps(
            {
                "login": {
                    "username": self.username,
                    "password": self.password,
                }
            }
        )
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )

        # {
        # "resp": {
        #     "status": "success",
        #     "respCode": "<integer>",
        #     "respMsg": "<string>"
        # },
        # "login": {
        #     "token": "<string>",
        #     "expire": "<integer>"
        # }
        # }

        # save the bearer token and time to expire
        login_resp = json.loads(response.text)

        self.login_token = login_resp["login"]["token"]
        self.login_epoch_time = login_resp["login"]["expire"]

        return self.login_token

    def logout_from_switch(self):
        url = self.make_url() + "logout"
        payload = {}
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.login_token,
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )

        # {
        # "resp": {
        #     "status": "failure",
        #     "respCode": "<integer>",
        #     "respMsg": "<string>"
        # }
        # }

        status = json.loads(response.text)["resp"]["status"]

        return status

    def __str__(self):
        return self.short_name
