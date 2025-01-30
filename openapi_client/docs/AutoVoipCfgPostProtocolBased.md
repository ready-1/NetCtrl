# AutoVoipCfgPostProtocolBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prioritization_type** | **str** |  | [default to 'traffic-class']
**class_value** | **int** | Class value:   * 6 max for traffic-class   * 7 max for remark  | [default to 6]
**mode** | **bool** | Auto VoIP mode of the Protocol base config for the specified port number | [default to False]

## Example

```python
from openapi_client.models.auto_voip_cfg_post_protocol_based import AutoVoipCfgPostProtocolBased

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVoipCfgPostProtocolBased from a JSON string
auto_voip_cfg_post_protocol_based_instance = AutoVoipCfgPostProtocolBased.from_json(json)
# print the JSON string representation of the object
print(AutoVoipCfgPostProtocolBased.to_json())

# convert the object into a dict
auto_voip_cfg_post_protocol_based_dict = auto_voip_cfg_post_protocol_based_instance.to_dict()
# create an instance of AutoVoipCfgPostProtocolBased from a dict
auto_voip_cfg_post_protocol_based_from_dict = AutoVoipCfgPostProtocolBased.from_dict(auto_voip_cfg_post_protocol_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
