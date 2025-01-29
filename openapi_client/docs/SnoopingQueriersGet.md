# SnoopingQueriersGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Configured IP address of querier | [optional] 
**admin_mode** | **str** | Querier enabled status | [optional] 
**expiry_interval** | **int** | Expiry interval of a snoop instance in seconds | [optional] 
**last_querier_address** | **str** | Last IP address detected for querier | [optional] 
**last_querier_version** | **int** | Last version detected for querier | [optional] 
**oper_max_resp_time** | **int** | Operational value of max response time in seconds | [optional] 
**oper_state** | **str** | Operational state of querier | [optional] 
**oper_version** | **int** | Operational version of querier | [optional] 
**query_interval** | **int** | Snooping query interval in seconds | [optional] 
**querier_version** | **int** | Configured version for querier | [optional] 
**vlan_address** | **str** | IP address configured for the querier. | [optional] 
**vlan_election_mode** | **str** | Configured snooping querier election mode for the VLAN ID | [optional] 
**vlan_mode** | **str** | Configured snooping querier mode for the VLAN ID | [optional] 

## Example

```python
from openapi_client.models.snooping_queriers_get import SnoopingQueriersGet

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingQueriersGet from a JSON string
snooping_queriers_get_instance = SnoopingQueriersGet.from_json(json)
# print the JSON string representation of the object
print(SnoopingQueriersGet.to_json())

# convert the object into a dict
snooping_queriers_get_dict = snooping_queriers_get_instance.to_dict()
# create an instance of SnoopingQueriersGet from a dict
snooping_queriers_get_from_dict = SnoopingQueriersGet.from_dict(snooping_queriers_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


