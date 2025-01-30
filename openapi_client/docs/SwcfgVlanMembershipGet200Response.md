# SwcfgVlanMembershipGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**vlan_membership** | [**SwcfgVlanMembership**](SwcfgVlanMembership.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_vlan_membership_get200_response import SwcfgVlanMembershipGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembershipGet200Response from a JSON string
swcfg_vlan_membership_get200_response_instance = SwcfgVlanMembershipGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembershipGet200Response.to_json())

# convert the object into a dict
swcfg_vlan_membership_get200_response_dict = swcfg_vlan_membership_get200_response_instance.to_dict()
# create an instance of SwcfgVlanMembershipGet200Response from a dict
swcfg_vlan_membership_get200_response_from_dict = SwcfgVlanMembershipGet200Response.from_dict(swcfg_vlan_membership_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
