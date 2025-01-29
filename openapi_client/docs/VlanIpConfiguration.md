# VlanIpConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_status** | **bool** | VLAN DHCP Status | 
**vlan_id** | **int** | VLAN ID | 
**ip_mtu** | **int** | Maximum size of IP packets sent on an interface | [default to 1500]

## Example

```python
from openapi_client.models.vlan_ip_configuration import VlanIpConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of VlanIpConfiguration from a JSON string
vlan_ip_configuration_instance = VlanIpConfiguration.from_json(json)
# print the JSON string representation of the object
print(VlanIpConfiguration.to_json())

# convert the object into a dict
vlan_ip_configuration_dict = vlan_ip_configuration_instance.to_dict()
# create an instance of VlanIpConfiguration from a dict
vlan_ip_configuration_from_dict = VlanIpConfiguration.from_dict(vlan_ip_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


