# SwcfgPortRtlimitBcast

Rate limit for broadcast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Rate limit for broadcast enabled or disabled | [default to False]
**threshold** | **int** | Rate limiting value for broadcast as a percentage | [default to 5]

## Example

```python
from openapi_client.models.swcfg_port_rtlimit_bcast import SwcfgPortRtlimitBcast

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPortRtlimitBcast from a JSON string
swcfg_port_rtlimit_bcast_instance = SwcfgPortRtlimitBcast.from_json(json)
# print the JSON string representation of the object
print(SwcfgPortRtlimitBcast.to_json())

# convert the object into a dict
swcfg_port_rtlimit_bcast_dict = swcfg_port_rtlimit_bcast_instance.to_dict()
# create an instance of SwcfgPortRtlimitBcast from a dict
swcfg_port_rtlimit_bcast_from_dict = SwcfgPortRtlimitBcast.from_dict(swcfg_port_rtlimit_bcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


