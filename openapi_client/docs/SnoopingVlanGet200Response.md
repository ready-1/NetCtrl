# SnoopingVlanGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**snooping_vlans** | [**List[SnoopingVlanInner]**](SnoopingVlanInner.md) |  | [optional]

## Example

```python
from openapi_client.models.snooping_vlan_get200_response import SnoopingVlanGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingVlanGet200Response from a JSON string
snooping_vlan_get200_response_instance = SnoopingVlanGet200Response.from_json(json)
# print the JSON string representation of the object
print(SnoopingVlanGet200Response.to_json())

# convert the object into a dict
snooping_vlan_get200_response_dict = snooping_vlan_get200_response_instance.to_dict()
# create an instance of SnoopingVlanGet200Response from a dict
snooping_vlan_get200_response_from_dict = SnoopingVlanGet200Response.from_dict(snooping_vlan_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
