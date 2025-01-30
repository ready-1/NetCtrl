# PoeConfigGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**poe_config** | [**PoeConfigGet**](PoeConfigGet.md) |  | [optional]

## Example

```python
from openapi_client.models.poe_config_get200_response import PoeConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PoeConfigGet200Response from a JSON string
poe_config_get200_response_instance = PoeConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print(PoeConfigGet200Response.to_json())

# convert the object into a dict
poe_config_get200_response_dict = poe_config_get200_response_instance.to_dict()
# create an instance of PoeConfigGet200Response from a dict
poe_config_get200_response_from_dict = PoeConfigGet200Response.from_dict(poe_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
