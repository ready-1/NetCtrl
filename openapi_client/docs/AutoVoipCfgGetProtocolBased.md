# AutoVoipCfgGetProtocolBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prioritization_type** | **str** |  | [optional] [default to 'traffic-class']
**class_value** | **int** | Class value:   * 6 max for traffic-class   * 7 max for remark  | [optional] [default to 6]
**mode** | **bool** | Auto VoIP mode of the Protocol base config for the specified port number | [optional] [default to False]
**status** | **bool** | Operational Status of protocol based Auto VoIP for the specified port number | [optional] [default to False]

## Example

```python
from openapi_client.models.auto_voip_cfg_get_protocol_based import AutoVoipCfgGetProtocolBased

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgGetProtocolBased from a JSON string
auto_voip_cfg_get_protocol_based_instance = AutoVoipCfgGetProtocolBased.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgGetProtocolBased.to_json())

# convert the object into a dict
auto_voip_cfg_get_protocol_based_dict = auto_voip_cfg_get_protocol_based_instance.to_dict()
# create an instance of AutoVoipCfgGetProtocolBased from a dict
auto_voip_cfg_get_protocol_based_from_dict = AutoVoipCfgGetProtocolBased.from_dict(auto_voip_cfg_get_protocol_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
