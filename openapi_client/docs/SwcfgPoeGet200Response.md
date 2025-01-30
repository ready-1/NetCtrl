# SwcfgPoeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**poe_port_config** | [**SwcfgPoe**](SwcfgPoe.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_poe_get200_response import SwcfgPoeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPoeGet200Response from a JSON string
swcfg_poe_get200_response_instance = SwcfgPoeGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwcfgPoeGet200Response.to_json())

# convert the object into a dict
swcfg_poe_get200_response_dict = swcfg_poe_get200_response_instance.to_dict()
# create an instance of SwcfgPoeGet200Response from a dict
swcfg_poe_get200_response_from_dict = SwcfgPoeGet200Response.from_dict(swcfg_poe_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
