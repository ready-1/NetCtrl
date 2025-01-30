# SwcfgPortRtlimitMcast

Rate limit for multicast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Rate limit for multicast enabled or disabled | [default to False]
**threshold** | **int** | Rate limiting value for multicast as a percentage | [default to 5]

## Example

```python
from openapi_client.models.swcfg_port_rtlimit_mcast import SwcfgPortRtlimitMcast

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPortRtlimitMcast from a JSON string
swcfg_port_rtlimit_mcast_instance = SwcfgPortRtlimitMcast.from_json(json)
# print the JSON string representation of the object
print(SwcfgPortRtlimitMcast.to_json())

# convert the object into a dict
swcfg_port_rtlimit_mcast_dict = swcfg_port_rtlimit_mcast_instance.to_dict()
# create an instance of SwcfgPortRtlimitMcast from a dict
swcfg_port_rtlimit_mcast_from_dict = SwcfgPortRtlimitMcast.from_dict(swcfg_port_rtlimit_mcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
