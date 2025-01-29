# Ptpv2GlobalPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptpv2_global** | [**Ptpv2Global**](Ptpv2Global.md) |  | [optional] 

## Example

```python
from openapi_client.models.ptpv2_global_post_request import Ptpv2GlobalPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ptpv2GlobalPostRequest from a JSON string
ptpv2_global_post_request_instance = Ptpv2GlobalPostRequest.from_json(json)
# print the JSON string representation of the object
print(Ptpv2GlobalPostRequest.to_json())

# convert the object into a dict
ptpv2_global_post_request_dict = ptpv2_global_post_request_instance.to_dict()
# create an instance of Ptpv2GlobalPostRequest from a dict
ptpv2_global_post_request_from_dict = Ptpv2GlobalPostRequest.from_dict(ptpv2_global_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


