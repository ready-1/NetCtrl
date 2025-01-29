# DeviceName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**location** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.device_name import DeviceName

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceName from a JSON string
device_name_instance = DeviceName.from_json(json)
# print the JSON string representation of the object
print(DeviceName.to_json())

# convert the object into a dict
device_name_dict = device_name_instance.to_dict()
# create an instance of DeviceName from a dict
device_name_from_dict = DeviceName.from_dict(device_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


