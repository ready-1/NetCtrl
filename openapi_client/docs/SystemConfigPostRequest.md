# SystemConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_config** | [**SystemConfigPost**](SystemConfigPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_config_post_request import SystemConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigPostRequest from a JSON string
system_config_post_request_instance = SystemConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(SystemConfigPostRequest.to_json())

# convert the object into a dict
system_config_post_request_dict = system_config_post_request_instance.to_dict()
# create an instance of SystemConfigPostRequest from a dict
system_config_post_request_from_dict = SystemConfigPostRequest.from_dict(system_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


