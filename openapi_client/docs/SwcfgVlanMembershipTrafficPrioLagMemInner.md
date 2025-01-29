# SwcfgVlanMembershipTrafficPrioLagMemInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portid** | **int** | Traffic priority and Port VLAN IDs (PVID) for these LAG ports. | [optional] 

## Example

```python
from openapi_client.models.swcfg_vlan_membership_traffic_prio_lag_mem_inner import SwcfgVlanMembershipTrafficPrioLagMemInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembershipTrafficPrioLagMemInner from a JSON string
swcfg_vlan_membership_traffic_prio_lag_mem_inner_instance = SwcfgVlanMembershipTrafficPrioLagMemInner.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembershipTrafficPrioLagMemInner.to_json())

# convert the object into a dict
swcfg_vlan_membership_traffic_prio_lag_mem_inner_dict = swcfg_vlan_membership_traffic_prio_lag_mem_inner_instance.to_dict()
# create an instance of SwcfgVlanMembershipTrafficPrioLagMemInner from a dict
swcfg_vlan_membership_traffic_prio_lag_mem_inner_from_dict = SwcfgVlanMembershipTrafficPrioLagMemInner.from_dict(swcfg_vlan_membership_traffic_prio_lag_mem_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


