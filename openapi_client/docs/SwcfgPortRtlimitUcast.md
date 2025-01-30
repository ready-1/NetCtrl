# SwcfgPortRtlimitUcast

Rate limit for unicast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Rate limit for unicast enabled or disabled | [default to False]
**threshold** | **int** | Rate limiting value for unicast as a percentage | [default to 5]

## Example

```python
from openapi_client.models.swcfg_port_rtlimit_ucast import SwcfgPortRtlimitUcast

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPortRtlimitUcast from a JSON string
swcfg_port_rtlimit_ucast_instance = SwcfgPortRtlimitUcast.from_json(json)
# print the JSON string representation of the object
print(SwcfgPortRtlimitUcast.to_json())

# convert the object into a dict
swcfg_port_rtlimit_ucast_dict = swcfg_port_rtlimit_ucast_instance.to_dict()
# create an instance of SwcfgPortRtlimitUcast from a dict
swcfg_port_rtlimit_ucast_from_dict = SwcfgPortRtlimitUcast.from_dict(swcfg_port_rtlimit_ucast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
