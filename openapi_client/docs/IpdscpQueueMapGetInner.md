# IpdscpQueueMapGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dscpid** | **int** | Class identifier for this DSCP | [optional] 
**dscpmap** | **int** | Assigned queue number | [optional] 

## Example

```python
from openapi_client.models.ipdscp_queue_map_get_inner import IpdscpQueueMapGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of IpdscpQueueMapGetInner from a JSON string
ipdscp_queue_map_get_inner_instance = IpdscpQueueMapGetInner.from_json(json)
# print the JSON string representation of the object
print(IpdscpQueueMapGetInner.to_json())

# convert the object into a dict
ipdscp_queue_map_get_inner_dict = ipdscp_queue_map_get_inner_instance.to_dict()
# create an instance of IpdscpQueueMapGetInner from a dict
ipdscp_queue_map_get_inner_from_dict = IpdscpQueueMapGetInner.from_dict(ipdscp_queue_map_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


