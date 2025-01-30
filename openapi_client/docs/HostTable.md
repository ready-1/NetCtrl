# HostTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | IP Address | [optional]
**mac_addr** | **str** | MAC Address | [optional]
**vlan_id** | **int** | VLAN ID | [optional]

## Example

```python
from openapi_client.models.host_table import HostTable

# TODO update the JSON string below
json = "{}"
# create an instance of HostTable from a JSON string
host_table_instance = HostTable.from_json(json)
# print the JSON string representation of the object
print(HostTable.to_json())

# convert the object into a dict
host_table_dict = host_table_instance.to_dict()
# create an instance of HostTable from a dict
host_table_from_dict = HostTable.from_dict(host_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
