# SwcfgVlanMembershipPvidMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portid** | **int** | Port VLAN IDs (PVID) assignments for these port interfaces. | [optional]

## Example

```python
from openapi_client.models.swcfg_vlan_membership_pvid_members_inner import SwcfgVlanMembershipPvidMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembershipPvidMembersInner from a JSON string
swcfg_vlan_membership_pvid_members_inner_instance = SwcfgVlanMembershipPvidMembersInner.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembershipPvidMembersInner.to_json())

# convert the object into a dict
swcfg_vlan_membership_pvid_members_inner_dict = swcfg_vlan_membership_pvid_members_inner_instance.to_dict()
# create an instance of SwcfgVlanMembershipPvidMembersInner from a dict
swcfg_vlan_membership_pvid_members_inner_from_dict = SwcfgVlanMembershipPvidMembersInner.from_dict(swcfg_vlan_membership_pvid_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
