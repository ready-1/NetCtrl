# SnoopingVlanInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | VLAN ID | [optional]
**family** | **str** | Snooping family | [optional]
**fast_leave_mode** | **str** | Snooping fast leave mode for the specified VLAN | [optional]
**vlan_mode** | **str** | Snooping mode for the specified VLAN | [optional]
**report_supp_mode** | **str** | Snooping report suppression mode for the specified VLAN | [optional]
**proxy_querier_mode** | **str** | Proxy Querier Admin mode for the specified VLAN. | [optional]
**group_membership_interval** | **int** | IGMP/MLD snooping group membership interval for the specified VLAN. | [optional]
**max_response_time** | **int** | IGMP/MLD snooping maximum response time for the specified VLAN. | [optional]

## Example

```python
from openapi_client.models.snooping_vlan_inner import SnoopingVlanInner

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingVlanInner from a JSON string
snooping_vlan_inner_instance = SnoopingVlanInner.from_json(json)
# print the JSON string representation of the object
print(SnoopingVlanInner.to_json())

# convert the object into a dict
snooping_vlan_inner_dict = snooping_vlan_inner_instance.to_dict()
# create an instance of SnoopingVlanInner from a dict
snooping_vlan_inner_from_dict = SnoopingVlanInner.from_dict(snooping_vlan_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
