# SnoopingQueriersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**snooping_queriers** | [**SnoopingQueriersGet**](SnoopingQueriersGet.md) |  | [optional] 

## Example

```python
from openapi_client.models.snooping_queriers_get200_response import SnoopingQueriersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingQueriersGet200Response from a JSON string
snooping_queriers_get200_response_instance = SnoopingQueriersGet200Response.from_json(json)
# print the JSON string representation of the object
print(SnoopingQueriersGet200Response.to_json())

# convert the object into a dict
snooping_queriers_get200_response_dict = snooping_queriers_get200_response_instance.to_dict()
# create an instance of SnoopingQueriersGet200Response from a dict
snooping_queriers_get200_response_from_dict = SnoopingQueriersGet200Response.from_dict(snooping_queriers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


