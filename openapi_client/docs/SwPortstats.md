# SwPortstats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_id** | **int** | Port Number | [optional] 
**switch_name** | **str** | Name of Switch | [optional] 
**my_desc** | **str** | Port description | [optional] 
**admin_mode** | **bool** | Admin Mode of port | [optional] 
**status** | **int** | Link Status:   * &#x60;0&#x60; &#x3D; LINK_UP   * &#x60;1&#x60; &#x3D; LINK_DOWN  | [optional] 
**poe_status** | **int** | PoE Status:   * &#x60;-1&#x60; &#x3D; STATUS_INVALID   * &#x60;0&#x60; &#x3D; STATUS_DISABLED   * &#x60;1&#x60; &#x3D; STATUS_SEARCHING   * &#x60;2&#x60; &#x3D; STATUS_DELIVERING_POWER   * &#x60;3&#x60; &#x3D; STATUS_TEST   * &#x60;4&#x60; &#x3D; STATUS_FAULT   * &#x60;5&#x60; &#x3D; STATUS_OTHER_FAULT   * &#x60;6&#x60; &#x3D; STATUS_REQUESTING_POWER   * &#x60;7&#x60; &#x3D; STATUS_OVERLOAD  | [optional] 
**mode** | **int** | Port Mode:   * &#x60;0&#x60; &#x3D; MODE_NONE   * &#x60;1&#x60; &#x3D; MODE_GENERAL   * &#x60;2&#x60; &#x3D; MODE_ACCESS   * &#x60;3&#x60; &#x3D; MODE_TRUNK   * &#x60;4&#x60; &#x3D; MODE_PRIVATE_HOST   * &#x60;5&#x60; &#x3D; MODE_PRIVATE_PROMISC  | [optional] 
**vlans** | **List[int]** |  | [optional] 
**traffic_rx** | **int** | Total number of bytes received | [optional] 
**traffic_tx** | **int** | Total number of bytes transmitted | [optional] 
**rx_mbps** | **str** | Current receive bit rate in Mbps | [optional] 
**tx_mbps** | **str** | Current transmit bit rate in Mbps | [optional] 
**crc_errors_rx** | **int** | Total numver of packets with CRC errors received | [optional] 
**errors_rx_tx** | **int** | Number of error packets | [optional] 
**drops_rx_tx** | **int** | Number of packets dropped | [optional] 
**port_mac_address** | **str** | Port MAC Address | [optional] 
**speed** | **int** | Interface Speed:   * &#x60;1&#x60; &#x3D; SPEED_AUTO_NEG   * &#x60;2&#x60; &#x3D; SPEED_HALF_100TX   * &#x60;3&#x60; &#x3D; SPEED_FULL_100TX   * &#x60;4&#x60; &#x3D; SPEED_HALF_10T   * &#x60;5&#x60; &#x3D; SPEED_FULL_10T   * &#x60;6&#x60; &#x3D; SPEED_FULL_100FX   * &#x60;7&#x60; &#x3D; SPEED_FULL_1000SX   * &#x60;8&#x60; &#x3D; SPEED_FULL_10GSX   * &#x60;9&#x60; &#x3D; SPEED_FULL_20GSX   * &#x60;10&#x60; &#x3D; SPEED_FULL_40GSX   * &#x60;11&#x60; &#x3D; SPEED_FULL_25GSX   * &#x60;12&#x60; &#x3D; SPEED_FULL_50GSX   * &#x60;13&#x60; &#x3D; SPEED_FULL_100GSX   * &#x60;14&#x60; &#x3D; SPEED_AAL5_155   * &#x60;15&#x60; &#x3D; SPEED_FULL_5FX   * &#x60;128&#x60; &#x3D; SPEED_FULL_2P5FX   * &#x60;129&#x60; &#x3D; SPEED_LAG   * &#x60;130&#x60; &#x3D; SPEED_UNKNOWN  | [optional] 
**duplex** | **int** | Interface Duplex mode:   * &#x60;0&#x60; &#x3D; half   * &#x60;1&#x60; &#x3D; full   * &#x60;65535&#x60; &#x3D; auto  | [optional] 
**frame_size** | **int** | Packets size measured in Maximum Transmission Units | [optional] 
**flow_control** | **bool** | Flow control enabled | [optional] 
**lacp_mode** | **bool** | LACP enabled | [optional] 
**mirrored** | **bool** | Port mirror enabled | [optional] 
**stp_status** | **bool** | STP admin mode enabled on the port | [optional] 
**port_state** | **int** | STP port state:   * &#x60;1&#x60; &#x3D; Discarding   * &#x60;2&#x60; &#x3D; Learning   * &#x60;3&#x60; &#x3D; Forwarding   * &#x60;4&#x60; &#x3D; Disabled   * &#x60;5&#x60; &#x3D; Manual forwarding   * &#x60;6&#x60; &#x3D; Not participate  | [optional] 
**opr_state** | **int** | Port operational state:   * &#x60;0&#x60; &#x3D; DIAG_PORT_DISABLE   * &#x60;1&#x60; &#x3D; DIAG_PORT_ENABLE   * &#x60;2&#x60; DIAG_PORT_D_DISABLE  | [optional] 
**power_limit_class** | **int** | PoE port power class:   * &#x60;0&#x60; &#x3D; INVALID   * &#x60;1&#x60; &#x3D; CLASS0   * &#x60;2&#x60; &#x3D; CLASS1   * &#x60;3&#x60; &#x3D; CLASS2   * &#x60;4&#x60; &#x3D; CLASS3   * &#x60;5&#x60; &#x3D; CLASS4  | [optional] 
**neighbor_info** | [**SwPortstatsNeighborInfo**](SwPortstatsNeighborInfo.md) |  | [optional] 
**port_auth_state** | **int** | Port authorization state:   * &#x60;1&#x60; &#x3D; Authorised   * &#x60;2&#x60; &#x3D; Unauthorised   * &#x60;3&#x60; &#x3D; N/A  | [optional] 

## Example

```python
from openapi_client.models.sw_portstats import SwPortstats

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortstats from a JSON string
sw_portstats_instance = SwPortstats.from_json(json)
# print the JSON string representation of the object
print(SwPortstats.to_json())

# convert the object into a dict
sw_portstats_dict = sw_portstats_instance.to_dict()
# create an instance of SwPortstats from a dict
sw_portstats_from_dict = SwPortstats.from_dict(sw_portstats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


