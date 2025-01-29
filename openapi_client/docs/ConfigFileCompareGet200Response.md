# ConfigFileCompareGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**config_file_compare** | [**ConfigFileCompare**](ConfigFileCompare.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_file_compare_get200_response import ConfigFileCompareGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFileCompareGet200Response from a JSON string
config_file_compare_get200_response_instance = ConfigFileCompareGet200Response.from_json(json)
# print the JSON string representation of the object
print(ConfigFileCompareGet200Response.to_json())

# convert the object into a dict
config_file_compare_get200_response_dict = config_file_compare_get200_response_instance.to_dict()
# create an instance of ConfigFileCompareGet200Response from a dict
config_file_compare_get200_response_from_dict = ConfigFileCompareGet200Response.from_dict(config_file_compare_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


