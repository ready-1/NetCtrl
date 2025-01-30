# VoiceVlanCfg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | Voice VLAN Config Mode:   * &#x60;0&#x60; &#x3D; Voice VLAN config disable   * &#x60;1&#x60; &#x3D; Voice VLAN config VLAN ID   * &#x60;2&#x60; &#x3D; Voice VLAN config DOT1P   * &#x60;3&#x60; &#x3D; Voice VLAN config none   * &#x60;4&#x60; &#x3D; Voice VLAN config untagged  | [default to 0]
**value** | **int** | DOT1P Priority | [default to 0]

## Example

```python
from openapi_client.models.voice_vlan_cfg import VoiceVlanCfg

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceVlanCfg from a JSON string
voice_vlan_cfg_instance = VoiceVlanCfg.from_json(json)
# print the JSON string representation of the object
print(VoiceVlanCfg.to_json())

# convert the object into a dict
voice_vlan_cfg_dict = voice_vlan_cfg_instance.to_dict()
# create an instance of VoiceVlanCfg from a dict
voice_vlan_cfg_from_dict = VoiceVlanCfg.from_dict(voice_vlan_cfg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
