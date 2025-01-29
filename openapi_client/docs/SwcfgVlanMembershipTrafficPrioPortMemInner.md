# SwcfgVlanMembershipTrafficPrioPortMemInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portid** | **int** | Traffic priority and Port VLAN IDs (PVID) for these physical ports | [optional] 

## Example

```python
from openapi_client.models.swcfg_vlan_membership_traffic_prio_port_mem_inner import SwcfgVlanMembershipTrafficPrioPortMemInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembershipTrafficPrioPortMemInner from a JSON string
swcfg_vlan_membership_traffic_prio_port_mem_inner_instance = SwcfgVlanMembershipTrafficPrioPortMemInner.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembershipTrafficPrioPortMemInner.to_json())

# convert the object into a dict
swcfg_vlan_membership_traffic_prio_port_mem_inner_dict = swcfg_vlan_membership_traffic_prio_port_mem_inner_instance.to_dict()
# create an instance of SwcfgVlanMembershipTrafficPrioPortMemInner from a dict
swcfg_vlan_membership_traffic_prio_port_mem_inner_from_dict = SwcfgVlanMembershipTrafficPrioPortMemInner.from_dict(swcfg_vlan_membership_traffic_prio_port_mem_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


