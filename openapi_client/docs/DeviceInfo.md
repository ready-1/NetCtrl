# DeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Switch display name | [optional] 
**serial_number** | **str** | Switch Serial Number | [optional] 
**mac_addr** | **str** | Switch MAC Address | [optional] 
**model** | **str** | Switch Model Number | [optional] 
**lan_ip_address** | **str** | LAN IP Address | [optional] 
**sw_ver** | **str** | Active firmware version | [optional] 
**last_reboot** | **str** | Time of last reboot with time zone information | [optional] 
**num_of_ports** | **int** | Total number of switch ports available | [optional] 
**num_of_active_ports** | **int** | Total number of currently active switch ports | [optional] 
**rstp_state** | **bool** | RSTP State | [optional] 
**memory_used** | **str** | Amount of RAM used in KBs | [optional] 
**memory_usage** | **str** | % of memory usage | [optional] 
**cpu_usage** | **str** | % of CPU usage | [optional] 
**fan_state** | **str** | Fan status | [optional] 
**poe_state** | **bool** | PoE enabled status | [optional] 
**up_time** | **str** | Up time of device | [optional] 
**temperature_sensors** | [**List[DeviceInfoTemperatureSensorsInner]**](DeviceInfoTemperatureSensorsInner.md) |  | [optional] 
**boot_version** | **str** | Bootcode version of the Switch. | [optional] 
**rx_data** | **int** | Total number of bytes received | [optional] 
**tx_data** | **int** | Total number of bytes transmitted | [optional] 
**admin_poe_power** | **int** | Admin PoE power as selected from Web UI (unit is mW) | [optional] 

## Example

```python
from openapi_client.models.device_info import DeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfo from a JSON string
device_info_instance = DeviceInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceInfo.to_json())

# convert the object into a dict
device_info_dict = device_info_instance.to_dict()
# create an instance of DeviceInfo from a dict
device_info_from_dict = DeviceInfo.from_dict(device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


