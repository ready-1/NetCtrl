Lksz24]AbN


import os, sys
import json
import requests
from django.db import models

from django.contrib.postgres.fields import JSONField

# Create your models here.
class Netgear(models.Model):
    short_name = models.CharField(max_length=100)
    in_band_ip = models.CharField(max_length=15)
    out_band_ip = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login_token = models.CharField(max_length=100, default="", blank=True)
    login_epoch_time = models.IntegerField(default=0, blank=True)
    current_switch_config = models.JSONField(blank=True, null=True)

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

        self.alive = False
        self.device_info = ""
        self.device_name = ""
        self.sw_device_name = ""
        self.sw_device_location = ""
        self.sw_model = ""
        self.sw_numOfPorts = 0

        poll_switch(self) # polls switch for device info


    def poll_switch(self):
        self.is_alive()
        if self.alive:
            self.device_info = self.get_device_info()
            self.device_name = self.get_device_name()

            self.sw_device_name = json.loads(self.device_name)["name"]
            self.sw_device_location = json.loads(self.device_name)["location"]
            self.sw_model = json.loads(self.device_info)["model"]
            self.sw_numOfPorts = json.loads(self.device_info)["numOfPorts"]

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
    
    def get_device_info(self):
        self.login_to_switch()
        url = self.make_url() + "device_info"

        payload = {}
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.login_token,
        }

        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        self.logout_from_switch()

        # {
        #   "resp": {
        #     "status": "failure",
        #     "respCode": "<integer>",
        #     "respMsg": "<string>"
        #   },
        #   "device_info": {
        #     "name": "<string>",
        #     "serialNumber": "<string>",
        #     "macAddr": "<string>",
        #     "model": "<string>",
        #     "lanIpAddress": "<string>",
        #     "swVer": "<string>",
        #     "lastReboot": "<string>",
        #     "numOfPorts": "<integer>",
        #     "numOfActivePorts": "<integer>",
        #     "rstpState": "<boolean>",
        #     "memoryUsed": "<string>",
        #     "memoryUsage": "<string>",
        #     "cpuUsage": "<string>",
        #     "fanState": "<string>",
        #     "poeState": "<boolean>",
        #     "upTime": "<string>",
        #     "temperatureSensors": [
        #       {
        #         "sensorNum": "<integer>",
        #         "sensorDesc": "<integer>",
        #         "sensorTemp": "<string>",
        #         "sensorState": "2"
        #       },
        #       {
        #         "sensorNum": "<integer>",
        #         "sensorDesc": "<integer>",
        #         "sensorTemp": "<string>",
        #         "sensorState": "1"
        #       }
        #     ],
        #     "bootVersion": "<string>",
        #     "rxData": "<integer>",
        #     "txData": "<integer>",
        #     "adminPoePower": "<integer>"
        #   }
        # }

        device_info_resp = json.loads(response.text)
        return json.dumps(device_info_resp["deviceInfo"], indent=4)
    
    def get_device_name(self):
        self.login_to_switch()
        url = self.make_url() + "device_name"

        payload = {}
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.login_token,
        }

        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        self.logout_from_switch()

        # {
        # "resp": {
        #     "status": "failure",
        #     "respCode": "<integer>",
        #     "respMsg": "<string>"
        # },
        # "deviceName": {
        #     "name": "<string>",
        #     "location": "<string>"
        # }
        # }

        device_name_resp = json.loads(response.text)
        return json.dumps(device_name_resp["deviceName"], indent=4)

    def get_system_config(self):
        pass

    def get_system_rfc1213(self):
        pass

    def __str__(self):
        return self.short_name
