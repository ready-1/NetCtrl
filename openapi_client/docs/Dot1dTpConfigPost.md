# Dot1dTpConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aging_time** | **int** | Aging time in seconds. | [default to 300]

## Example

```python
from openapi_client.models.dot1d_tp_config_post import Dot1dTpConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dTpConfigPost from a JSON string
dot1d_tp_config_post_instance = Dot1dTpConfigPost.from_json(json)
# print the JSON string representation of the object
print(Dot1dTpConfigPost.to_json())

# convert the object into a dict
dot1d_tp_config_post_dict = dot1d_tp_config_post_instance.to_dict()
# create an instance of Dot1dTpConfigPost from a dict
dot1d_tp_config_post_from_dict = Dot1dTpConfigPost.from_dict(dot1d_tp_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


