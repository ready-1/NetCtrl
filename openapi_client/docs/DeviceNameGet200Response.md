# DeviceNameGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**device_name** | [**DeviceName**](DeviceName.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_name_get200_response import DeviceNameGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNameGet200Response from a JSON string
device_name_get200_response_instance = DeviceNameGet200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceNameGet200Response.to_json())

# convert the object into a dict
device_name_get200_response_dict = device_name_get200_response_instance.to_dict()
# create an instance of DeviceNameGet200Response from a dict
device_name_get200_response_from_dict = DeviceNameGet200Response.from_dict(device_name_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


