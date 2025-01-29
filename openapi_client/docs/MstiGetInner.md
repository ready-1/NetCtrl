# MstiGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mst_id** | **int** | MST Instance | [optional] 
**priority** | **int** | Instance priority | [optional] 
**vlans** | [**List[MstiGetInnerVlansInner]**](MstiGetInnerVlansInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.msti_get_inner import MstiGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of MstiGetInner from a JSON string
msti_get_inner_instance = MstiGetInner.from_json(json)
# print the JSON string representation of the object
print(MstiGetInner.to_json())

# convert the object into a dict
msti_get_inner_dict = msti_get_inner_instance.to_dict()
# create an instance of MstiGetInner from a dict
msti_get_inner_from_dict = MstiGetInner.from_dict(msti_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


