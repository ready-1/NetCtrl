# LogoutPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]

## Example

```python
from openapi_client.models.logout_post200_response import LogoutPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutPost200Response from a JSON string
logout_post200_response_instance = LogoutPost200Response.from_json(json)
# print the JSON string representation of the object
print(LogoutPost200Response.to_json())

# convert the object into a dict
logout_post200_response_dict = logout_post200_response_instance.to_dict()
# create an instance of LogoutPost200Response from a dict
logout_post200_response_from_dict = LogoutPost200Response.from_dict(logout_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
