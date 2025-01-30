# DualImageStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**dual_image_status** | [**DualImageStatus**](DualImageStatus.md) |  | [optional]

## Example

```python
from openapi_client.models.dual_image_status_get200_response import DualImageStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DualImageStatusGet200Response from a JSON string
dual_image_status_get200_response_instance = DualImageStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(DualImageStatusGet200Response.to_json())

# convert the object into a dict
dual_image_status_get200_response_dict = dual_image_status_get200_response_instance.to_dict()
# create an instance of DualImageStatusGet200Response from a dict
dual_image_status_get200_response_from_dict = DualImageStatusGet200Response.from_dict(dual_image_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
