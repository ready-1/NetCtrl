# MstiGetInnerVlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | VLAN ID WRT Instance | [optional]
**type** | **str** | VLAN Type | [optional]
**name** | **str** | VLAN Name | [optional]

## Example

```python
from openapi_client.models.msti_get_inner_vlans_inner import MstiGetInnerVlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of MstiGetInnerVlansInner from a JSON string
msti_get_inner_vlans_inner_instance = MstiGetInnerVlansInner.from_json(json)
# print the JSON string representation of the object
print(MstiGetInnerVlansInner.to_json())

# convert the object into a dict
msti_get_inner_vlans_inner_dict = msti_get_inner_vlans_inner_instance.to_dict()
# create an instance of MstiGetInnerVlansInner from a dict
msti_get_inner_vlans_inner_from_dict = MstiGetInnerVlansInner.from_dict(msti_get_inner_vlans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
