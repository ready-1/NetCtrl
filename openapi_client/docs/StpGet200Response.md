# StpGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**spanning_tree** | [**Stp**](Stp.md) |  | [optional] 

## Example

```python
from openapi_client.models.stp_get200_response import StpGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StpGet200Response from a JSON string
stp_get200_response_instance = StpGet200Response.from_json(json)
# print the JSON string representation of the object
print(StpGet200Response.to_json())

# convert the object into a dict
stp_get200_response_dict = stp_get200_response_instance.to_dict()
# create an instance of StpGet200Response from a dict
stp_get200_response_from_dict = StpGet200Response.from_dict(stp_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


