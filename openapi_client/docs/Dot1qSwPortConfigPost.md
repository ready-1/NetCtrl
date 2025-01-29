# Dot1qSwPortConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_vlan** | **int** | Set access VLAN ID for the interface | 
**allowed_vlan_list** | **List[str]** | VLANs ID &#x60;#&#x60; or &#x60;all&#x60; VLANs allowed | 
**config_mode** | **str** | Switchport Configuration Mode for a port | 
**native_vlan** | **str** | Native VLAN ID for a port | 

## Example

```python
from openapi_client.models.dot1q_sw_port_config_post import Dot1qSwPortConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1qSwPortConfigPost from a JSON string
dot1q_sw_port_config_post_instance = Dot1qSwPortConfigPost.from_json(json)
# print the JSON string representation of the object
print(Dot1qSwPortConfigPost.to_json())

# convert the object into a dict
dot1q_sw_port_config_post_dict = dot1q_sw_port_config_post_instance.to_dict()
# create an instance of Dot1qSwPortConfigPost from a dict
dot1q_sw_port_config_post_from_dict = Dot1qSwPortConfigPost.from_dict(dot1q_sw_port_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


