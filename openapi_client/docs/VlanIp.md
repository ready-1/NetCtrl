# VlanIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | VLAN ID | [optional] 
**dhcp_status** | **bool** | Enable VLAN DHCP client | [optional] 
**ip_addr** | **str** | VLAN IP address | [optional] 
**ip_mask** | **str** | VLAN subnet mask | [optional] 
**ip_mtu** | **int** | VLAN Maximum Transmission Unit (MTU) size | [optional] 
**vlan_routing** | **bool** | Enable VLAN routing | [optional] 

## Example

```python
from openapi_client.models.vlan_ip import VlanIp

# TODO update the JSON string below
json = "{}"
# create an instance of VlanIp from a JSON string
vlan_ip_instance = VlanIp.from_json(json)
# print the JSON string representation of the object
print(VlanIp.to_json())

# convert the object into a dict
vlan_ip_dict = vlan_ip_instance.to_dict()
# create an instance of VlanIp from a dict
vlan_ip_from_dict = VlanIp.from_dict(vlan_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


