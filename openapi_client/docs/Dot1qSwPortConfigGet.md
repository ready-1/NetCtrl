# Dot1qSwPortConfigGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Physical or logical interface in slot/port format | [optional]
**access_vlan** | **int** | Access VLAN ID for the interface | [optional]
**allowed_vlan_list** | **List[str]** |  | [optional]
**dynamically_added_vlan_list** | **str** | Dynamically Added VLANs for the interface | [optional]
**forbidden_vlan_list** | **str** | Forbidden VLANs for the interface | [optional]
**config_mode** | **str** | Switchport Configuration Mode for the interface | [optional]
**native_vlan** | **int** | Native VLAN ID for the interface | [optional]
**tagged_vlan_list** | **List[str]** |  | [optional]
**untagged_vlan_list** | **List[str]** |  | [optional]

## Example

```python
from openapi_client.models.dot1q_sw_port_config_get import Dot1qSwPortConfigGet

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1qSwPortConfigGet from a JSON string
dot1q_sw_port_config_get_instance = Dot1qSwPortConfigGet.from_json(json)
# print the JSON string representation of the object
print(Dot1qSwPortConfigGet.to_json())

# convert the object into a dict
dot1q_sw_port_config_get_dict = dot1q_sw_port_config_get_instance.to_dict()
# create an instance of Dot1qSwPortConfigGet from a dict
dot1q_sw_port_config_get_from_dict = Dot1qSwPortConfigGet.from_dict(dot1q_sw_port_config_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
