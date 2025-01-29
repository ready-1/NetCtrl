# SwcfgPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Port Number | 
**description** | **str** | Port description label | 
**port_type** | **int** | Port configuration type:   * &#x60;0&#x60; &#x3D; MODE_NONE   * &#x60;1&#x60; &#x3D; MODE_GENERAL   * &#x60;2&#x60; &#x3D; MODE_ACCESS   * &#x60;3&#x60; &#x3D; MODE_TRUNK   * &#x60;4&#x60; &#x3D; MODE_PRIVATE_HOST   * &#x60;5&#x60; &#x3D; MODE_PRIVATE_PROMISC  | [default to 1]
**admin_mode** | **bool** | Enable physical port interface | [default to True]
**port_speed** | **int** | Port link speed:   * &#x60;0&#x60; &#x3D; auto   * &#x60;1&#x60; &#x3D; SP10   * &#x60;2&#x60; &#x3D; SP100   * &#x60;3&#x60; &#x3D; SP1000   * &#x60;4&#x60; &#x3D; SP10G  | [optional] [default to 0]
**duplex_mode** | **int** | Duplex Mode:   * &#x60;2&#x60; &#x3D; auto   * &#x60;1&#x60; &#x3D; full   * &#x60;0&#x60; &#x3D; half  | [optional] [default to 2]
**link_status** | **int** | Link up or down Status (read-only):   * &#x60;0&#x60; &#x3D; Up   * &#x60;1&#x60; &#x3D; Down  | [optional] [default to 1]
**link_trap** | **bool** | Enable link trap | [optional] [default to True]
**max_frame_size** | **int** | Max frame size | [optional] [default to 1518]
**is_po_e** | **bool** | Port is PoE capable | [default to True]
**tx_rate** | **int** | Traffic shaping rate for the interface as a percentage. 0% means traffic is Unlimited. 100% means traffic is Blocked/Limited. | [default to 0]
**rtlimit_ucast** | [**SwcfgPortRtlimitUcast**](SwcfgPortRtlimitUcast.md) |  | 
**rtlimit_mcast** | [**SwcfgPortRtlimitMcast**](SwcfgPortRtlimitMcast.md) |  | 
**rtlimit_bcast** | [**SwcfgPortRtlimitBcast**](SwcfgPortRtlimitBcast.md) |  | 
**port_vlan_id** | **int** | Port&#39;s VLAN ID | [default to 1]
**def_vlan_prio** | **int** | Default VLAN priority | [default to 0]
**schedule_name** | **str** | Name of the schedule | [optional] 

## Example

```python
from openapi_client.models.swcfg_port import SwcfgPort

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPort from a JSON string
swcfg_port_instance = SwcfgPort.from_json(json)
# print the JSON string representation of the object
print(SwcfgPort.to_json())

# convert the object into a dict
swcfg_port_dict = swcfg_port_instance.to_dict()
# create an instance of SwcfgPort from a dict
swcfg_port_from_dict = SwcfgPort.from_dict(swcfg_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


