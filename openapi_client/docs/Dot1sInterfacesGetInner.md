# Dot1sInterfacesGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **int** | Port interface number | [optional] 
**bpdu_filter_mode** | **bool** | BPDU filter mode | [optional] [default to False]
**bpdu_flood_mode** | **bool** | BPDU flood mode | [optional] [default to False]
**intf_edge_port_mode** | **bool** | Interface edge port mode | [optional] [default to False]
**intf_guard_mode** | **int** | STP Guard Mode:   * &#x60;0&#x60; &#x3D; Loop   * &#x60;1&#x60; &#x3D; Root   * &#x60;2&#x60; &#x3D; None  | [optional] 
**intf_mode** | **int** | Interface mode | [optional] 

## Example

```python
from openapi_client.models.dot1s_interfaces_get_inner import Dot1sInterfacesGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1sInterfacesGetInner from a JSON string
dot1s_interfaces_get_inner_instance = Dot1sInterfacesGetInner.from_json(json)
# print the JSON string representation of the object
print(Dot1sInterfacesGetInner.to_json())

# convert the object into a dict
dot1s_interfaces_get_inner_dict = dot1s_interfaces_get_inner_instance.to_dict()
# create an instance of Dot1sInterfacesGetInner from a dict
dot1s_interfaces_get_inner_from_dict = Dot1sInterfacesGetInner.from_dict(dot1s_interfaces_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


