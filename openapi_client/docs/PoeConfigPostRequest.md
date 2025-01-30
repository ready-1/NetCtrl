# PoeConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poe_config** | [**PoeConfigPost**](PoeConfigPost.md) |  | [optional]

## Example

```python
from openapi_client.models.poe_config_post_request import PoeConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PoeConfigPostRequest from a JSON string
poe_config_post_request_instance = PoeConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(PoeConfigPostRequest.to_json())

# convert the object into a dict
poe_config_post_request_dict = poe_config_post_request_instance.to_dict()
# create an instance of PoeConfigPostRequest from a dict
poe_config_post_request_from_dict = PoeConfigPostRequest.from_dict(poe_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
