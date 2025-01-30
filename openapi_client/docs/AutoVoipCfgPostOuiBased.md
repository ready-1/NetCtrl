# AutoVoipCfgPostOuiBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | Auto VoIP VLAN ID |
**priority** | **int** |  | [default to 5]
**mode** | **bool** | Auto VoIP mode of the OUI base config for the specified port number | [default to False]

## Example

```python
from openapi_client.models.auto_voip_cfg_post_oui_based import AutoVoipCfgPostOuiBased

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgPostOuiBased from a JSON string
auto_voip_cfg_post_oui_based_instance = AutoVoipCfgPostOuiBased.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgPostOuiBased.to_json())

# convert the object into a dict
auto_voip_cfg_post_oui_based_dict = auto_voip_cfg_post_oui_based_instance.to_dict()
# create an instance of AutoVoipCfgPostOuiBased from a dict
auto_voip_cfg_post_oui_based_from_dict = AutoVoipCfgPostOuiBased.from_dict(auto_voip_cfg_post_oui_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
