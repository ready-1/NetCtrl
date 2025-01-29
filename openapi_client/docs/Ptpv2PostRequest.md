# Ptpv2PostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptpv2** | [**Ptpv2Post**](Ptpv2Post.md) |  | [optional] 

## Example

```python
from openapi_client.models.ptpv2_post_request import Ptpv2PostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ptpv2PostRequest from a JSON string
ptpv2_post_request_instance = Ptpv2PostRequest.from_json(json)
# print the JSON string representation of the object
print(Ptpv2PostRequest.to_json())

# convert the object into a dict
ptpv2_post_request_dict = ptpv2_post_request_instance.to_dict()
# create an instance of Ptpv2PostRequest from a dict
ptpv2_post_request_from_dict = Ptpv2PostRequest.from_dict(ptpv2_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


