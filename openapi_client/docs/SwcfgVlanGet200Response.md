# SwcfgVlanGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**switch_config_vlan** | [**SwcfgVlan**](SwcfgVlan.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_vlan_get200_response import SwcfgVlanGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanGet200Response from a JSON string
swcfg_vlan_get200_response_instance = SwcfgVlanGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanGet200Response.to_json())

# convert the object into a dict
swcfg_vlan_get200_response_dict = swcfg_vlan_get200_response_instance.to_dict()
# create an instance of SwcfgVlanGet200Response from a dict
swcfg_vlan_get200_response_from_dict = SwcfgVlanGet200Response.from_dict(swcfg_vlan_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
