# SwPortstatsNeighborInfo

Neighbor connected device Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Neighbor name | [optional] 
**description** | **str** | Neighbor description | [optional] 
**capabilities** | **str** | Neighbor capabilites | [optional] 
**chassis_id** | **str** | Neighbor chassis ID | [optional] 
**chassis_id_subtype** | **int** | Neighbor chassis subtype:   * &#x60;1&#x60; &#x3D; SUBTYPE_CHASSIS_COMP   * &#x60;2&#x60; &#x3D; SUBTYPE_INTF_ALIAS   * &#x60;3&#x60; &#x3D; SUBTYPE_PORT_COMP   * &#x60;4&#x60; &#x3D; SUBTYPE_MAC_ADDR   * &#x60;5&#x60; &#x3D; SUBTYPE_NET_ADDR   * &#x60;6&#x60; &#x3D; SUBTYPE_INTF_NAME   * &#x60;7&#x60; &#x3D; SUBTYPE_LOCAL  | [optional] 
**port_id** | **str** | Neighbor port ID | [optional] 
**port_id_subtype** | **int** | Neighbor port subtype:   * &#x60;1&#x60; &#x3D; SUBTYPE_INTF_ALIAS   * &#x60;2&#x60; &#x3D; SUBTYPE_PORT_COMP   * &#x60;3&#x60; &#x3D; SUBTYPE_MAC_ADDR   * &#x60;4&#x60; &#x3D; SUBTYPE_NET_ADDR   * &#x60;5&#x60; &#x3D; SUBTYPE_INTF_NAME   * &#x60;6&#x60; &#x3D; SUBTYPE_AGENT_ID   * &#x60;7&#x60; &#x3D; SUBTYPE_LOCAL  | [optional] 
**port_description** | **str** | Neighbor port description | [optional] 
**mgmt_ip_address** | **str** | Neighbor management IP Address | [optional] 

## Example

```python
from openapi_client.models.sw_portstats_neighbor_info import SwPortstatsNeighborInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortstatsNeighborInfo from a JSON string
sw_portstats_neighbor_info_instance = SwPortstatsNeighborInfo.from_json(json)
# print the JSON string representation of the object
print(SwPortstatsNeighborInfo.to_json())

# convert the object into a dict
sw_portstats_neighbor_info_dict = sw_portstats_neighbor_info_instance.to_dict()
# create an instance of SwPortstatsNeighborInfo from a dict
sw_portstats_neighbor_info_from_dict = SwPortstatsNeighborInfo.from_dict(sw_portstats_neighbor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


