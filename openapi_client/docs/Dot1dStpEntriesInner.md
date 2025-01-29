# Dot1dStpEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port interface number | [optional] 
**priority** | **int** | Spanning Tree port priority | [optional] 
**state** | **str** | Spanning Tree port state | [optional] 
**path_cost** | **int** | Spanning Tree path cost for the port. | [optional] 
**designated_root** | **str** | Spanning Tree designated root for the switch. | [optional] 
**designated_cost** | **int** | Spanning Tree designated cost for the port | [optional] 
**designated_bridge** | **str** | Spanning Tree designated bridge for the port | [optional] 
**designated_port** | **str** | Spanning Tree designated port ID | [optional] 

## Example

```python
from openapi_client.models.dot1d_stp_entries_inner import Dot1dStpEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dStpEntriesInner from a JSON string
dot1d_stp_entries_inner_instance = Dot1dStpEntriesInner.from_json(json)
# print the JSON string representation of the object
print(Dot1dStpEntriesInner.to_json())

# convert the object into a dict
dot1d_stp_entries_inner_dict = dot1d_stp_entries_inner_instance.to_dict()
# create an instance of Dot1dStpEntriesInner from a dict
dot1d_stp_entries_inner_from_dict = Dot1dStpEntriesInner.from_dict(dot1d_stp_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


