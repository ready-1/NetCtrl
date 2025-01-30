# Dot1pQueueMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority assigned to this class | [optional]
**queuemap** | **int** | Assigned queue number | [optional]

## Example

```python
from openapi_client.models.dot1p_queue_map_inner import Dot1pQueueMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1pQueueMapInner from a JSON string
dot1p_queue_map_inner_instance = Dot1pQueueMapInner.from_json(json)
# print the JSON string representation of the object
print(Dot1pQueueMapInner.to_json())

# convert the object into a dict
dot1p_queue_map_inner_dict = dot1p_queue_map_inner_instance.to_dict()
# create an instance of Dot1pQueueMapInner from a dict
dot1p_queue_map_inner_from_dict = Dot1pQueueMapInner.from_dict(dot1p_queue_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
