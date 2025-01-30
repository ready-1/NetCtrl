# LldpRemoteDevicesMgmtAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | List of types | [optional]
**address** | **str** | List of IP addresses | [optional]

## Example

```python
from openapi_client.models.lldp_remote_devices_mgmt_addresses_inner import LldpRemoteDevicesMgmtAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LldpRemoteDevicesMgmtAddressesInner from a JSON string
lldp_remote_devices_mgmt_addresses_inner_instance = LldpRemoteDevicesMgmtAddressesInner.from_json(json)
# print the JSON string representation of the object
print(LldpRemoteDevicesMgmtAddressesInner.to_json())

# convert the object into a dict
lldp_remote_devices_mgmt_addresses_inner_dict = lldp_remote_devices_mgmt_addresses_inner_instance.to_dict()
# create an instance of LldpRemoteDevicesMgmtAddressesInner from a dict
lldp_remote_devices_mgmt_addresses_inner_from_dict = LldpRemoteDevicesMgmtAddressesInner.from_dict(lldp_remote_devices_mgmt_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
