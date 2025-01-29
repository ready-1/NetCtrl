# LldpRemoteDevices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | LLDP ID Number | [optional] 
**if_index** | **int** | Internal interface number | [optional] 
**remote_id** | **int** | Identifier for device on remote system | [optional] 
**chassis_id** | **str** | Remote device hardware platform | [optional] 
**chassis_id_subtype** | **int** | Chassis ID field subtype:   * &#x60;1&#x60; &#x3D; Chassis component   * &#x60;2&#x60; &#x3D; Interface alias   * &#x60;3&#x60; &#x3D; Port component   * &#x60;4&#x60; &#x3D; MAC address   * &#x60;5&#x60; &#x3D; Network address   * &#x60;6&#x60; &#x3D; Interface name   * &#x60;7&#x60; &#x3D; Local  | [optional] 
**remote_port_id** | **str** | Device port that transmitted LLDP data | [optional] 
**remote_port_id_subtype** | **int** | Remote port field subtype:   * &#x60;1&#x60; &#x3D; Chassis component   * &#x60;2&#x60; &#x3D; Interface alias   * &#x60;3&#x60; &#x3D; Port component   * &#x60;4&#x60; &#x3D; MAC address   * &#x60;5&#x60; &#x3D; Network address   * &#x60;6&#x60; &#x3D; Interface name   * &#x60;7&#x60; &#x3D; Local  | [optional] 
**remote_port_desc** | **str** | Remote system port description | [optional] 
**remote_sys_name** | **str** | Name assigned to the device in the remote system | [optional] 
**remote_sys_desc** | **str** | Description assigned to the device in the remote system | [optional] 
**sys_capabilities_supported** | **str** | List of primary functions supported by the remote system | [optional] 
**sys_capabilities_enabled** | **str** | List of primary functions enabled on the remote system | [optional] 
**mgmt_addresses** | [**List[LldpRemoteDevicesMgmtAddressesInner]**](LldpRemoteDevicesMgmtAddressesInner.md) |  | [optional] 
**remote_ttl** | **int** | Remote device Time To Live information offset | [optional] 

## Example

```python
from openapi_client.models.lldp_remote_devices import LldpRemoteDevices

# TODO update the JSON string below
json = "{}"
# create an instance of LldpRemoteDevices from a JSON string
lldp_remote_devices_instance = LldpRemoteDevices.from_json(json)
# print the JSON string representation of the object
print(LldpRemoteDevices.to_json())

# convert the object into a dict
lldp_remote_devices_dict = lldp_remote_devices_instance.to_dict()
# create an instance of LldpRemoteDevices from a dict
lldp_remote_devices_from_dict = LldpRemoteDevices.from_dict(lldp_remote_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


