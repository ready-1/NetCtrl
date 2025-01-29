# SnoopingInterfacesGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **int** | Port interface ID | [optional] 
**fast_leave_admin_mode** | **str** | IGMP/MLD Snooping Fast leave admin mode | [optional] 
**group_membership_interval** | **int** | IGMP/MLD group membership interval | [optional] 
**intf_mode** | **str** | Snooping mode | [optional] 
**proxy_querier_mode** | **str** | Proxy Querier Admin mode for the specified interface | [optional] 
**response_time** | **int** | Query response time for the specified interface | [optional] 
**family** | **str** | Snooping family | [optional] 

## Example

```python
from openapi_client.models.snooping_interfaces_get_inner import SnoopingInterfacesGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingInterfacesGetInner from a JSON string
snooping_interfaces_get_inner_instance = SnoopingInterfacesGetInner.from_json(json)
# print the JSON string representation of the object
print(SnoopingInterfacesGetInner.to_json())

# convert the object into a dict
snooping_interfaces_get_inner_dict = snooping_interfaces_get_inner_instance.to_dict()
# create an instance of SnoopingInterfacesGetInner from a dict
snooping_interfaces_get_inner_from_dict = SnoopingInterfacesGetInner.from_dict(snooping_interfaces_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


