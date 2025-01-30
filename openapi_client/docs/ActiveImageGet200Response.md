# ActiveImageGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**active_image** | [**ActiveImageGet**](ActiveImageGet.md) |  | [optional]

## Example

```python
from openapi_client.models.active_image_get200_response import ActiveImageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveImageGet200Response from a JSON string
active_image_get200_response_instance = ActiveImageGet200Response.from_json(json)
# print the JSON string representation of the object
print(ActiveImageGet200Response.to_json())

# convert the object into a dict
active_image_get200_response_dict = active_image_get200_response_instance.to_dict()
# create an instance of ActiveImageGet200Response from a dict
active_image_get200_response_from_dict = ActiveImageGet200Response.from_dict(active_image_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
