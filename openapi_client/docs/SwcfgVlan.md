# SwcfgVlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | VLAN ID | 
**name** | **str** | VLAN Name | 
**voice_vlan_state** | **bool** | Voice VLAN status | [optional] [default to False]
**auto_voip_state** | **bool** | AutoVoIP | [optional] [default to False]
**auto_video_state** | **bool** | Auto Video | [optional] [default to False]
**igmp_config** | [**SwcfgVlanIgmpConfig**](SwcfgVlanIgmpConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.swcfg_vlan import SwcfgVlan

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlan from a JSON string
swcfg_vlan_instance = SwcfgVlan.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlan.to_json())

# convert the object into a dict
swcfg_vlan_dict = swcfg_vlan_instance.to_dict()
# create an instance of SwcfgVlan from a dict
swcfg_vlan_from_dict = SwcfgVlan.from_dict(swcfg_vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


