# Dot1sInterfacesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **int** | Port interface number | [optional]
**bpdu_filter_mode** | **bool** | BPDU filter mode | [optional]
**bpdu_flood_mode** | **bool** | BPDU flood mode | [optional]
**intf_edge_port_mode** | **bool** | Interface edge port mode | [optional]
**intf_guard_mode** | **int** | STP Gaurd Mode:   * &#x60;0&#x60; &#x3D; Loop   * &#x60;1&#x60; &#x3D; Root   * &#x60;2&#x60; &#x3D; None  | [optional]
**intf_mode** | **bool** | Interface Mode | [optional]

## Example

```python
from openapi_client.models.dot1s_interfaces_post import Dot1sInterfacesPost

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1sInterfacesPost from a JSON string
dot1s_interfaces_post_instance = Dot1sInterfacesPost.from_json(json)
# print the JSON string representation of the object
print(Dot1sInterfacesPost.to_json())

# convert the object into a dict
dot1s_interfaces_post_dict = dot1s_interfaces_post_instance.to_dict()
# create an instance of Dot1sInterfacesPost from a dict
dot1s_interfaces_post_from_dict = Dot1sInterfacesPost.from_dict(dot1s_interfaces_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
