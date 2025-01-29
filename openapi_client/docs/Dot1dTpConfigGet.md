# Dot1dTpConfigGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learned_entry_discards** | **int** | Learned entry | [optional] 
**aging_time** | **int** | Aging time in seconds. | [optional] [default to 300]

## Example

```python
from openapi_client.models.dot1d_tp_config_get import Dot1dTpConfigGet

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dTpConfigGet from a JSON string
dot1d_tp_config_get_instance = Dot1dTpConfigGet.from_json(json)
# print the JSON string representation of the object
print(Dot1dTpConfigGet.to_json())

# convert the object into a dict
dot1d_tp_config_get_dict = dot1d_tp_config_get_instance.to_dict()
# create an instance of Dot1dTpConfigGet from a dict
dot1d_tp_config_get_from_dict = Dot1dTpConfigGet.from_dict(dot1d_tp_config_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


