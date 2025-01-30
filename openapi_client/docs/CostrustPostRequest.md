# CostrustPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costrust** | [**Costrust**](Costrust.md) |  | [optional]

## Example

```python
from openapi_client.models.costrust_post_request import CostrustPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CostrustPostRequest from a JSON string
costrust_post_request_instance = CostrustPostRequest.from_json(json)
# print the JSON string representation of the object
print(CostrustPostRequest.to_json())

# convert the object into a dict
costrust_post_request_dict = costrust_post_request_instance.to_dict()
# create an instance of CostrustPostRequest from a dict
costrust_post_request_from_dict = CostrustPostRequest.from_dict(costrust_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
