# SystemRfc1213Get200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**system_rfc1213** | [**SystemRfc1213Get**](SystemRfc1213Get.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_rfc1213_get200_response import SystemRfc1213Get200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRfc1213Get200Response from a JSON string
system_rfc1213_get200_response_instance = SystemRfc1213Get200Response.from_json(json)
# print the JSON string representation of the object
print(SystemRfc1213Get200Response.to_json())

# convert the object into a dict
system_rfc1213_get200_response_dict = system_rfc1213_get200_response_instance.to_dict()
# create an instance of SystemRfc1213Get200Response from a dict
system_rfc1213_get200_response_from_dict = SystemRfc1213Get200Response.from_dict(system_rfc1213_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


