# Dot1dBaseConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_bridge_address** | **str** | Base bridge address | [optional]
**base_num_ports** | **int** | Base number ports | [optional]
**base_type** | **int** | Base type | [optional]

## Example

```python
from openapi_client.models.dot1d_base_config import Dot1dBaseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dBaseConfig from a JSON string
dot1d_base_config_instance = Dot1dBaseConfig.from_json(json)
# print the JSON string representation of the object
print(Dot1dBaseConfig.to_json())

# convert the object into a dict
dot1d_base_config_dict = dot1d_base_config_instance.to_dict()
# create an instance of Dot1dBaseConfig from a dict
dot1d_base_config_from_dict = Dot1dBaseConfig.from_dict(dot1d_base_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
