# SwcfgVlanPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_config_vlan** | [**SwcfgVlan**](SwcfgVlan.md) |  | [optional]

## Example

```python
from openapi_client.models.swcfg_vlan_post_request import SwcfgVlanPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanPostRequest from a JSON string
swcfg_vlan_post_request_instance = SwcfgVlanPostRequest.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanPostRequest.to_json())

# convert the object into a dict
swcfg_vlan_post_request_dict = swcfg_vlan_post_request_instance.to_dict()
# create an instance of SwcfgVlanPostRequest from a dict
swcfg_vlan_post_request_from_dict = SwcfgVlanPostRequest.from_dict(swcfg_vlan_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
