# SnoopingConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snooping_config** | [**SnoopingConfigPost**](SnoopingConfigPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.snooping_config_post_request import SnoopingConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingConfigPostRequest from a JSON string
snooping_config_post_request_instance = SnoopingConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(SnoopingConfigPostRequest.to_json())

# convert the object into a dict
snooping_config_post_request_dict = snooping_config_post_request_instance.to_dict()
# create an instance of SnoopingConfigPostRequest from a dict
snooping_config_post_request_from_dict = SnoopingConfigPostRequest.from_dict(snooping_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


