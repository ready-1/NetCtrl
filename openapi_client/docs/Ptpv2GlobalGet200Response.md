# Ptpv2GlobalGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**ptpv2_global** | [**Ptpv2Global**](Ptpv2Global.md) |  | [optional] 

## Example

```python
from openapi_client.models.ptpv2_global_get200_response import Ptpv2GlobalGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Ptpv2GlobalGet200Response from a JSON string
ptpv2_global_get200_response_instance = Ptpv2GlobalGet200Response.from_json(json)
# print the JSON string representation of the object
print(Ptpv2GlobalGet200Response.to_json())

# convert the object into a dict
ptpv2_global_get200_response_dict = ptpv2_global_get200_response_instance.to_dict()
# create an instance of Ptpv2GlobalGet200Response from a dict
ptpv2_global_get200_response_from_dict = Ptpv2GlobalGet200Response.from_dict(ptpv2_global_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


