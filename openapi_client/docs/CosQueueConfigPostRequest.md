# CosQueueConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos_queue_config** | [**List[CosQueueConfigInner]**](CosQueueConfigInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.cos_queue_config_post_request import CosQueueConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CosQueueConfigPostRequest from a JSON string
cos_queue_config_post_request_instance = CosQueueConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(CosQueueConfigPostRequest.to_json())

# convert the object into a dict
cos_queue_config_post_request_dict = cos_queue_config_post_request_instance.to_dict()
# create an instance of CosQueueConfigPostRequest from a dict
cos_queue_config_post_request_from_dict = CosQueueConfigPostRequest.from_dict(cos_queue_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


