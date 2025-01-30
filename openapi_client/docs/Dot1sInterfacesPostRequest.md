# Dot1sInterfacesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot1s_interfaces** | [**Dot1sInterfacesPost**](Dot1sInterfacesPost.md) |  | [optional]

## Example

```python
from openapi_client.models.dot1s_interfaces_post_request import Dot1sInterfacesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1sInterfacesPostRequest from a JSON string
dot1s_interfaces_post_request_instance = Dot1sInterfacesPostRequest.from_json(json)
# print the JSON string representation of the object
print(Dot1sInterfacesPostRequest.to_json())

# convert the object into a dict
dot1s_interfaces_post_request_dict = dot1s_interfaces_post_request_instance.to_dict()
# create an instance of Dot1sInterfacesPostRequest from a dict
dot1s_interfaces_post_request_from_dict = Dot1sInterfacesPostRequest.from_dict(dot1s_interfaces_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
