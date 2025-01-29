# SnoopingInterfacesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snooping_interfaces** | [**SnoopingInterfacesPost**](SnoopingInterfacesPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.snooping_interfaces_post_request import SnoopingInterfacesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingInterfacesPostRequest from a JSON string
snooping_interfaces_post_request_instance = SnoopingInterfacesPostRequest.from_json(json)
# print the JSON string representation of the object
print(SnoopingInterfacesPostRequest.to_json())

# convert the object into a dict
snooping_interfaces_post_request_dict = snooping_interfaces_post_request_instance.to_dict()
# create an instance of SnoopingInterfacesPostRequest from a dict
snooping_interfaces_post_request_from_dict = SnoopingInterfacesPostRequest.from_dict(snooping_interfaces_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


