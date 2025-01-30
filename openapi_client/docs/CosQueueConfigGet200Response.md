# CosQueueConfigGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**cos_queue_config** | [**List[CosQueueConfigInner]**](CosQueueConfigInner.md) |  | [optional]

## Example

```python
from openapi_client.models.cos_queue_config_get200_response import CosQueueConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CosQueueConfigGet200Response from a JSON string
cos_queue_config_get200_response_instance = CosQueueConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print(CosQueueConfigGet200Response.to_json())

# convert the object into a dict
cos_queue_config_get200_response_dict = cos_queue_config_get200_response_instance.to_dict()
# create an instance of CosQueueConfigGet200Response from a dict
cos_queue_config_get200_response_from_dict = CosQueueConfigGet200Response.from_dict(cos_queue_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
