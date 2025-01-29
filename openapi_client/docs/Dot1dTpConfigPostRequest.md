# Dot1dTpConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot1d_tp_config** | [**Dot1dTpConfigPost**](Dot1dTpConfigPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.dot1d_tp_config_post_request import Dot1dTpConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dTpConfigPostRequest from a JSON string
dot1d_tp_config_post_request_instance = Dot1dTpConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(Dot1dTpConfigPostRequest.to_json())

# convert the object into a dict
dot1d_tp_config_post_request_dict = dot1d_tp_config_post_request_instance.to_dict()
# create an instance of Dot1dTpConfigPostRequest from a dict
dot1d_tp_config_post_request_from_dict = Dot1dTpConfigPostRequest.from_dict(dot1d_tp_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


