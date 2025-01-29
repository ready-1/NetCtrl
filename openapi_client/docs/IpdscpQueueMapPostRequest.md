# IpdscpQueueMapPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipdscp_queue_map** | [**List[IpdscpQueueMapGetInner]**](IpdscpQueueMapGetInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.ipdscp_queue_map_post_request import IpdscpQueueMapPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IpdscpQueueMapPostRequest from a JSON string
ipdscp_queue_map_post_request_instance = IpdscpQueueMapPostRequest.from_json(json)
# print the JSON string representation of the object
print(IpdscpQueueMapPostRequest.to_json())

# convert the object into a dict
ipdscp_queue_map_post_request_dict = ipdscp_queue_map_post_request_instance.to_dict()
# create an instance of IpdscpQueueMapPostRequest from a dict
ipdscp_queue_map_post_request_from_dict = IpdscpQueueMapPostRequest.from_dict(ipdscp_queue_map_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


