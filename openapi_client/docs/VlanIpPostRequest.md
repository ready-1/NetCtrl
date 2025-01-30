# VlanIpPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_ip** | [**VlanIp**](VlanIp.md) |  | [optional]

## Example

```python
from openapi_client.models.vlan_ip_post_request import VlanIpPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VlanIpPostRequest from a JSON string
vlan_ip_post_request_instance = VlanIpPostRequest.from_json(json)
# print the JSON string representation of the object
print(VlanIpPostRequest.to_json())

# convert the object into a dict
vlan_ip_post_request_dict = vlan_ip_post_request_instance.to_dict()
# create an instance of VlanIpPostRequest from a dict
vlan_ip_post_request_from_dict = VlanIpPostRequest.from_dict(vlan_ip_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
