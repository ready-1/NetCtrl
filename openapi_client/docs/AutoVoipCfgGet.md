# AutoVoipCfgGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | Auto VoIP VLAN ID | [optional]
**supported_channels** | **int** | Count of max no of supported Voice channels | [optional] [default to 288]
**used_channels** | **int** | No of voice channels used | [optional] [default to 0]
**protocol_based** | [**AutoVoipCfgGetProtocolBased**](AutoVoipCfgGetProtocolBased.md) |  | [optional]
**oui_based** | [**AutoVoipCfgGetOuiBased**](AutoVoipCfgGetOuiBased.md) |  | [optional]

## Example

```python
from openapi_client.models.auto_voip_cfg_get import AutoVoipCfgGet

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgGet from a JSON string
auto_voip_cfg_get_instance = AutoVoipCfgGet.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgGet.to_json())

# convert the object into a dict
auto_voip_cfg_get_dict = auto_voip_cfg_get_instance.to_dict()
# create an instance of AutoVoipCfgGet from a dict
auto_voip_cfg_get_from_dict = AutoVoipCfgGet.from_dict(auto_voip_cfg_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
