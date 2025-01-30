# SwcfgPoePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poe_port_config** | [**SwcfgPoe**](SwcfgPoe.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_poe_post_request import SwcfgPoePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPoePostRequest from a JSON string
swcfg_poe_post_request_instance = SwcfgPoePostRequest.from_json(json)
# print the JSON string representation of the object
print(SwcfgPoePostRequest.to_json())

# convert the object into a dict
swcfg_poe_post_request_dict = swcfg_poe_post_request_instance.to_dict()
# create an instance of SwcfgPoePostRequest from a dict
swcfg_poe_post_request_from_dict = SwcfgPoePostRequest.from_dict(swcfg_poe_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
