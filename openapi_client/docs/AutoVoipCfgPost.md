# AutoVoipCfgPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_based** | [**AutoVoipCfgPostProtocolBased**](AutoVoipCfgPostProtocolBased.md) |  | 
**oui_based** | [**AutoVoipCfgPostOuiBased**](AutoVoipCfgPostOuiBased.md) |  | 

## Example

```python
from openapi_client.models.auto_voip_cfg_post import AutoVoipCfgPost

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgPost from a JSON string
auto_voip_cfg_post_instance = AutoVoipCfgPost.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgPost.to_json())

# convert the object into a dict
auto_voip_cfg_post_dict = auto_voip_cfg_post_instance.to_dict()
# create an instance of AutoVoipCfgPost from a dict
auto_voip_cfg_post_from_dict = AutoVoipCfgPost.from_dict(auto_voip_cfg_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


