# SwcfgVlanMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlanid** | **int** | VLAN ID | 
**port_members** | **List[object]** |  | 
**lag_members** | **List[object]** |  | 
**traffic_prio** | **int** | Traffic Priority of VLAN | 
**traffic_prio_port_mem** | [**List[SwcfgVlanMembershipTrafficPrioPortMemInner]**](SwcfgVlanMembershipTrafficPrioPortMemInner.md) |  | 
**traffic_prio_lag_mem** | [**List[SwcfgVlanMembershipTrafficPrioLagMemInner]**](SwcfgVlanMembershipTrafficPrioLagMemInner.md) |  | 
**pvid_members** | [**List[SwcfgVlanMembershipPvidMembersInner]**](SwcfgVlanMembershipPvidMembersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.swcfg_vlan_membership import SwcfgVlanMembership

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembership from a JSON string
swcfg_vlan_membership_instance = SwcfgVlanMembership.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembership.to_json())

# convert the object into a dict
swcfg_vlan_membership_dict = swcfg_vlan_membership_instance.to_dict()
# create an instance of SwcfgVlanMembership from a dict
swcfg_vlan_membership_from_dict = SwcfgVlanMembership.from_dict(swcfg_vlan_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


