# IpRouteTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_hop_intf** | **str** | Name of interface for next hop | [optional]
**route_mask** | **str** | Route mask | [optional]
**next_hop_addr** | **str** | IP address for next hop | [optional]
**route_type** | **str** | Type of route | [optional]
**route_proto** | **str** | Learned route protocol | [optional]
**route_dest** | **str** | Next destination | [optional]
**metric** | **int** | Routing metric | [optional]
**route_pref** | **int** | Preference of route | [optional]

## Example

```python
from openapi_client.models.ip_route_table import IpRouteTable

# TODO update the JSON string below
json = "{}"
# create an instance of IpRouteTable from a JSON string
ip_route_table_instance = IpRouteTable.from_json(json)
# print the JSON string representation of the object
print(IpRouteTable.to_json())

# convert the object into a dict
ip_route_table_dict = ip_route_table_instance.to_dict()
# create an instance of IpRouteTable from a dict
ip_route_table_from_dict = IpRouteTable.from_dict(ip_route_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
