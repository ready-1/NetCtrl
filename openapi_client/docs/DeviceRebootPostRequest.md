# DeviceRebootPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_reboot** | [**DeviceReboot**](DeviceReboot.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_reboot_post_request import DeviceRebootPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRebootPostRequest from a JSON string
device_reboot_post_request_instance = DeviceRebootPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceRebootPostRequest.to_json())

# convert the object into a dict
device_reboot_post_request_dict = device_reboot_post_request_instance.to_dict()
# create an instance of DeviceRebootPostRequest from a dict
device_reboot_post_request_from_dict = DeviceRebootPostRequest.from_dict(device_reboot_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


