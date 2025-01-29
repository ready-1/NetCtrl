# DeviceCableTestGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**cable_test_status** | [**DeviceCableTest**](DeviceCableTest.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_cable_test_get200_response import DeviceCableTestGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCableTestGet200Response from a JSON string
device_cable_test_get200_response_instance = DeviceCableTestGet200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceCableTestGet200Response.to_json())

# convert the object into a dict
device_cable_test_get200_response_dict = device_cable_test_get200_response_instance.to_dict()
# create an instance of DeviceCableTestGet200Response from a dict
device_cable_test_get200_response_from_dict = DeviceCableTestGet200Response.from_dict(device_cable_test_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


