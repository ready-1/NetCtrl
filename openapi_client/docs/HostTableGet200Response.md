# HostTableGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**host_table** | [**List[HostTable]**](HostTable.md) |  | [optional] 

## Example

```python
from openapi_client.models.host_table_get200_response import HostTableGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HostTableGet200Response from a JSON string
host_table_get200_response_instance = HostTableGet200Response.from_json(json)
# print the JSON string representation of the object
print(HostTableGet200Response.to_json())

# convert the object into a dict
host_table_get200_response_dict = host_table_get200_response_instance.to_dict()
# create an instance of HostTableGet200Response from a dict
host_table_get200_response_from_dict = HostTableGet200Response.from_dict(host_table_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


