# SnoopingInterfacesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **int** | Port interface ID | 
**family** | **str** | Snooping family | 
**fast_leave_admin_mode** | **str** | IGMP/MLD Snooping Fast leave admin mode | 
**group_membership_interval** | **int** | IGMP/MLD group membership interval | 
**intf_mode** | **str** | Snooping mode | 
**proxy_querier_mode** | **str** | Proxy Querier Admin mode for the specified interface | 
**response_time** | **int** | Query response time for the specified interface | 

## Example

```python
from openapi_client.models.snooping_interfaces_post import SnoopingInterfacesPost

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingInterfacesPost from a JSON string
snooping_interfaces_post_instance = SnoopingInterfacesPost.from_json(json)
# print the JSON string representation of the object
print(SnoopingInterfacesPost.to_json())

# convert the object into a dict
snooping_interfaces_post_dict = snooping_interfaces_post_instance.to_dict()
# create an instance of SnoopingInterfacesPost from a dict
snooping_interfaces_post_from_dict = SnoopingInterfacesPost.from_dict(snooping_interfaces_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


