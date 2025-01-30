# DeviceReboot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_secs** | **int** | Delay reboot for t seconds | [default to 2]

## Example

```python
from openapi_client.models.device_reboot import DeviceReboot

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceReboot from a JSON string
device_reboot_instance = DeviceReboot.from_json(json)
# print the JSON string representation of the object
print(DeviceReboot.to_json())

# convert the object into a dict
device_reboot_dict = device_reboot_instance.to_dict()
# create an instance of DeviceReboot from a dict
device_reboot_from_dict = DeviceReboot.from_dict(device_reboot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
