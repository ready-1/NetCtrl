# DeviceNamePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | [**DeviceName**](DeviceName.md) |  | [optional]

## Example

```python
from openapi_client.models.device_name_post_request import DeviceNamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNamePostRequest from a JSON string
device_name_post_request_instance = DeviceNamePostRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceNamePostRequest.to_json())

# convert the object into a dict
device_name_post_request_dict = device_name_post_request_instance.to_dict()
# create an instance of DeviceNamePostRequest from a dict
device_name_post_request_from_dict = DeviceNamePostRequest.from_dict(device_name_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
