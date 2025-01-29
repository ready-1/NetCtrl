# VoiceVlanGlbCfg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_mode** | **bool** | Global Voice VLAN feature setting | [default to True]

## Example

```python
from openapi_client.models.voice_vlan_glb_cfg import VoiceVlanGlbCfg

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceVlanGlbCfg from a JSON string
voice_vlan_glb_cfg_instance = VoiceVlanGlbCfg.from_json(json)
# print the JSON string representation of the object
print(VoiceVlanGlbCfg.to_json())

# convert the object into a dict
voice_vlan_glb_cfg_dict = voice_vlan_glb_cfg_instance.to_dict()
# create an instance of VoiceVlanGlbCfg from a dict
voice_vlan_glb_cfg_from_dict = VoiceVlanGlbCfg.from_dict(voice_vlan_glb_cfg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


