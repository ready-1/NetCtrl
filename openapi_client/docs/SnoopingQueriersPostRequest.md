# SnoopingQueriersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snooping_queriers** | [**SnoopingQueriersPost**](SnoopingQueriersPost.md) |  | [optional]

## Example

```python
from openapi_client.models.snooping_queriers_post_request import SnoopingQueriersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingQueriersPostRequest from a JSON string
snooping_queriers_post_request_instance = SnoopingQueriersPostRequest.from_json(json)
# print the JSON string representation of the object
print(SnoopingQueriersPostRequest.to_json())

# convert the object into a dict
snooping_queriers_post_request_dict = snooping_queriers_post_request_instance.to_dict()
# create an instance of SnoopingQueriersPostRequest from a dict
snooping_queriers_post_request_from_dict = SnoopingQueriersPostRequest.from_dict(snooping_queriers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
