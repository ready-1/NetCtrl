# FiberOpticsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**fiber_optics** | [**FiberOptics**](FiberOptics.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiber_optics_get200_response import FiberOpticsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FiberOpticsGet200Response from a JSON string
fiber_optics_get200_response_instance = FiberOpticsGet200Response.from_json(json)
# print the JSON string representation of the object
print(FiberOpticsGet200Response.to_json())

# convert the object into a dict
fiber_optics_get200_response_dict = fiber_optics_get200_response_instance.to_dict()
# create an instance of FiberOpticsGet200Response from a dict
fiber_optics_get200_response_from_dict = FiberOpticsGet200Response.from_dict(fiber_optics_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


