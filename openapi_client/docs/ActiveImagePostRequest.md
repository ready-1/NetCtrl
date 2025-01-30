# ActiveImagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_image** | [**ActiveImagePost**](ActiveImagePost.md) |  | [optional]

## Example

```python
from openapi_client.models.active_image_post_request import ActiveImagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveImagePostRequest from a JSON string
active_image_post_request_instance = ActiveImagePostRequest.from_json(json)
# print the JSON string representation of the object
print(ActiveImagePostRequest.to_json())

# convert the object into a dict
active_image_post_request_dict = active_image_post_request_instance.to_dict()
# create an instance of ActiveImagePostRequest from a dict
active_image_post_request_from_dict = ActiveImagePostRequest.from_dict(active_image_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
