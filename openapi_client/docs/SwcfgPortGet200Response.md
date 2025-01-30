# SwcfgPortGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_port_config** | [**SwcfgPort**](SwcfgPort.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_port_get200_response import SwcfgPortGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPortGet200Response from a JSON string
swcfg_port_get200_response_instance = SwcfgPortGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwcfgPortGet200Response.to_json())

# convert the object into a dict
swcfg_port_get200_response_dict = swcfg_port_get200_response_instance.to_dict()
# create an instance of SwcfgPortGet200Response from a dict
swcfg_port_get200_response_from_dict = SwcfgPortGet200Response.from_dict(swcfg_port_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
