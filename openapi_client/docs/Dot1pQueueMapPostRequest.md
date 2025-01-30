# Dot1pQueueMapPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot1p_queue_map** | [**List[Dot1pQueueMapInner]**](Dot1pQueueMapInner.md) |  | [optional]

## Example

```python
from openapi_client.models.dot1p_queue_map_post_request import Dot1pQueueMapPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1pQueueMapPostRequest from a JSON string
dot1p_queue_map_post_request_instance = Dot1pQueueMapPostRequest.from_json(json)
# print the JSON string representation of the object
print(Dot1pQueueMapPostRequest.to_json())

# convert the object into a dict
dot1p_queue_map_post_request_dict = dot1p_queue_map_post_request_instance.to_dict()
# create an instance of Dot1pQueueMapPostRequest from a dict
dot1p_queue_map_post_request_from_dict = Dot1pQueueMapPostRequest.from_dict(dot1p_queue_map_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
