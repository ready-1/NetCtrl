# SwPortmirroringSrcPortInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intf_type** | **int** | Source port capture type:   * &#x60;0&#x60; &#x3D; INTF_TYPE_PHY   * &#x60;1&#x60; &#x3D; INTF_TYPE_CPU   * &#x60;2&#x60; &#x3D; INTF_TYPE_LAG   * &#x60;3&#x60; &#x3D; INTF_TYPE_VLAN   * &#x60;4&#x60; &#x3D; INTF_TYPE_LOOPBACK   * &#x60;5&#x60; &#x3D; INTF_TYPE_TUNNEL   * &#x60;6&#x60; &#x3D; INTF_TYPE_SERVICE_PORT   * &#x60;7&#x60; &#x3D; INTF_TYPE_OTHER   * &#x60;8&#x60; &#x3D; INTF_TYPE_ANY  |
**intf_num** | **int** | Source port interface number |
**direction** | **int** | Source port capture direction:   * &#x60;1&#x60; &#x3D; BIDIRECTIONAL   * &#x60;2&#x60; &#x3D; INGRESS   * &#x60;3&#x60; &#x3D; EGRESS   * &#x60;4&#x60; &#x3D; SFLOW  |

## Example

```python
from openapi_client.models.sw_portmirroring_src_port_inner import SwPortmirroringSrcPortInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortmirroringSrcPortInner from a JSON string
sw_portmirroring_src_port_inner_instance = SwPortmirroringSrcPortInner.from_json(json)
# print the JSON string representation of the object
print(SwPortmirroringSrcPortInner.to_json())

# convert the object into a dict
sw_portmirroring_src_port_inner_dict = sw_portmirroring_src_port_inner_instance.to_dict()
# create an instance of SwPortmirroringSrcPortInner from a dict
sw_portmirroring_src_port_inner_from_dict = SwPortmirroringSrcPortInner.from_dict(sw_portmirroring_src_port_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
