# SystemConfigGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**system_config** | [**SystemConfigGet**](SystemConfigGet.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_config_get200_response import SystemConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigGet200Response from a JSON string
system_config_get200_response_instance = SystemConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print(SystemConfigGet200Response.to_json())

# convert the object into a dict
system_config_get200_response_dict = system_config_get200_response_instance.to_dict()
# create an instance of SystemConfigGet200Response from a dict
system_config_get200_response_from_dict = SystemConfigGet200Response.from_dict(system_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


