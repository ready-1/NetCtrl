# AutoVoipCfgGetOuiBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] [default to 5]
**mode** | **bool** | Auto VoIP mode of the OUI base config for the specified port number | [optional] [default to False]
**status** | **bool** | Operational Status of OUI based Auto VoIP for the specified port number | [optional] [default to False]

## Example

```python
from openapi_client.models.auto_voip_cfg_get_oui_based import AutoVoipCfgGetOuiBased

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgGetOuiBased from a JSON string
auto_voip_cfg_get_oui_based_instance = AutoVoipCfgGetOuiBased.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgGetOuiBased.to_json())

# convert the object into a dict
auto_voip_cfg_get_oui_based_dict = auto_voip_cfg_get_oui_based_instance.to_dict()
# create an instance of AutoVoipCfgGetOuiBased from a dict
auto_voip_cfg_get_oui_based_from_dict = AutoVoipCfgGetOuiBased.from_dict(auto_voip_cfg_get_oui_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
