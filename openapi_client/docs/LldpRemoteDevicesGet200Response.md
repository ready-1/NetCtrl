# LldpRemoteDevicesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lldp_remote_devices** | [**LldpRemoteDevices**](LldpRemoteDevices.md) |  | [optional] 

## Example

```python
from openapi_client.models.lldp_remote_devices_get200_response import LldpRemoteDevicesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LldpRemoteDevicesGet200Response from a JSON string
lldp_remote_devices_get200_response_instance = LldpRemoteDevicesGet200Response.from_json(json)
# print the JSON string representation of the object
print(LldpRemoteDevicesGet200Response.to_json())

# convert the object into a dict
lldp_remote_devices_get200_response_dict = lldp_remote_devices_get200_response_instance.to_dict()
# create an instance of LldpRemoteDevicesGet200Response from a dict
lldp_remote_devices_get200_response_from_dict = LldpRemoteDevicesGet200Response.from_dict(lldp_remote_devices_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


