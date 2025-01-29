# FdbsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **int** | Interface entry (slot/port) | [optional] 
**vlan_id** | **int** | VLAN ID of the entry | [optional] 
**mac** | **str** | MAC Address of the entry | [optional] 
**entry_type** | **int** | Fdb entry type:   * &#x60;0&#x60; &#x3D; Static   * &#x60;1&#x60; &#x3D; Learned   * &#x60;2&#x60; &#x3D; Management   * &#x60;3&#x60; &#x3D; GMRP Learned   * &#x60;4&#x60; &#x3D; Self   * &#x60;5&#x60; &#x3D; Dot1x Static   * &#x60;6&#x60; &#x3D; Dot1ag Static   * &#x60;7&#x60; &#x3D; Routing Intf address   * &#x60;8&#x60; &#x3D; Address is learned, but not guaranteed to be in HW (relevant for SW learning)   * &#x60;9&#x60; &#x3D; FIP Snooping Learned   * &#x60;10&#x60; &#x3D; CP client MAC Address   * &#x60;11&#x60; &#x3D; ethcfm Static   * &#x60;12&#x60; &#x3D; Y.1731 Static  | [optional] 

## Example

```python
from openapi_client.models.fdbs_inner import FdbsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FdbsInner from a JSON string
fdbs_inner_instance = FdbsInner.from_json(json)
# print the JSON string representation of the object
print(FdbsInner.to_json())

# convert the object into a dict
fdbs_inner_dict = fdbs_inner_instance.to_dict()
# create an instance of FdbsInner from a dict
fdbs_inner_from_dict = FdbsInner.from_dict(fdbs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


