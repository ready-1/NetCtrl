# FdbsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**fdb_stats** | [**List[FdbsInner]**](FdbsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.fdbs_get200_response import FdbsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FdbsGet200Response from a JSON string
fdbs_get200_response_instance = FdbsGet200Response.from_json(json)
# print the JSON string representation of the object
print(FdbsGet200Response.to_json())

# convert the object into a dict
fdbs_get200_response_dict = fdbs_get200_response_instance.to_dict()
# create an instance of FdbsGet200Response from a dict
fdbs_get200_response_from_dict = FdbsGet200Response.from_dict(fdbs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


