# IpdscpQueueMapGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**ipdscp_queue_map** | [**List[IpdscpQueueMapGetInner]**](IpdscpQueueMapGetInner.md) |  | [optional]

## Example

```python
from openapi_client.models.ipdscp_queue_map_get200_response import IpdscpQueueMapGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IpdscpQueueMapGet200Response from a JSON string
ipdscp_queue_map_get200_response_instance = IpdscpQueueMapGet200Response.from_json(json)
# print the JSON string representation of the object
print(IpdscpQueueMapGet200Response.to_json())

# convert the object into a dict
ipdscp_queue_map_get200_response_dict = ipdscp_queue_map_get200_response_instance.to_dict()
# create an instance of IpdscpQueueMapGet200Response from a dict
ipdscp_queue_map_get200_response_from_dict = IpdscpQueueMapGet200Response.from_dict(ipdscp_queue_map_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
