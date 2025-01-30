# Dot1pQueueMapGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**dot1p_queue_map** | [**List[Dot1pQueueMapInner]**](Dot1pQueueMapInner.md) |  | [optional]

## Example

```python
from openapi_client.models.dot1p_queue_map_get200_response import Dot1pQueueMapGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1pQueueMapGet200Response from a JSON string
dot1p_queue_map_get200_response_instance = Dot1pQueueMapGet200Response.from_json(json)
# print the JSON string representation of the object
print(Dot1pQueueMapGet200Response.to_json())

# convert the object into a dict
dot1p_queue_map_get200_response_dict = dot1p_queue_map_get200_response_instance.to_dict()
# create an instance of Dot1pQueueMapGet200Response from a dict
dot1p_queue_map_get200_response_from_dict = Dot1pQueueMapGet200Response.from_dict(dot1p_queue_map_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
