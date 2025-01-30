# SwcfgVlanIgmpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**igmp_state** | **bool** | IGMP state for the VLAN | [optional]

## Example

```python
from openapi_client.models.swcfg_vlan_igmp_config import SwcfgVlanIgmpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanIgmpConfig from a JSON string
swcfg_vlan_igmp_config_instance = SwcfgVlanIgmpConfig.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanIgmpConfig.to_json())

# convert the object into a dict
swcfg_vlan_igmp_config_dict = swcfg_vlan_igmp_config_instance.to_dict()
# create an instance of SwcfgVlanIgmpConfig from a dict
swcfg_vlan_igmp_config_from_dict = SwcfgVlanIgmpConfig.from_dict(swcfg_vlan_igmp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
