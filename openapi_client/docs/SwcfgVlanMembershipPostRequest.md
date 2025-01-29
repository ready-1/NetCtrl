# SwcfgVlanMembershipPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_membership** | [**SwcfgVlanMembership**](SwcfgVlanMembership.md) |  | [optional] 

## Example

```python
from openapi_client.models.swcfg_vlan_membership_post_request import SwcfgVlanMembershipPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgVlanMembershipPostRequest from a JSON string
swcfg_vlan_membership_post_request_instance = SwcfgVlanMembershipPostRequest.from_json(json)
# print the JSON string representation of the object
print(SwcfgVlanMembershipPostRequest.to_json())

# convert the object into a dict
swcfg_vlan_membership_post_request_dict = swcfg_vlan_membership_post_request_instance.to_dict()
# create an instance of SwcfgVlanMembershipPostRequest from a dict
swcfg_vlan_membership_post_request_from_dict = SwcfgVlanMembershipPostRequest.from_dict(swcfg_vlan_membership_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


