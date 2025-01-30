# Dot1qSwPortConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot1q_sw_port_config** | [**Dot1qSwPortConfigPost**](Dot1qSwPortConfigPost.md) |  | [optional]

## Example

```python
from openapi_client.models.dot1q_sw_port_config_post_request import Dot1qSwPortConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1qSwPortConfigPostRequest from a JSON string
dot1q_sw_port_config_post_request_instance = Dot1qSwPortConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(Dot1qSwPortConfigPostRequest.to_json())

# convert the object into a dict
dot1q_sw_port_config_post_request_dict = dot1q_sw_port_config_post_request_instance.to_dict()
# create an instance of Dot1qSwPortConfigPostRequest from a dict
dot1q_sw_port_config_post_request_from_dict = Dot1qSwPortConfigPostRequest.from_dict(dot1q_sw_port_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
