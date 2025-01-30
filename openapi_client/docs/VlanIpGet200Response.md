# VlanIpGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**vlan_ip** | [**List[VlanIp]**](VlanIp.md) |  | [optional]

## Example

```python
from openapi_client.models.vlan_ip_get200_response import VlanIpGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VlanIpGet200Response from a JSON string
vlan_ip_get200_response_instance = VlanIpGet200Response.from_json(json)
# print the JSON string representation of the object
print(VlanIpGet200Response.to_json())

# convert the object into a dict
vlan_ip_get200_response_dict = vlan_ip_get200_response_instance.to_dict()
# create an instance of VlanIpGet200Response from a dict
vlan_ip_get200_response_from_dict = VlanIpGet200Response.from_dict(vlan_ip_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
