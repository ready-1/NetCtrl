# SnoopingConfigGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Snooping family | [optional] 
**admin_mode** | **str** | IGMP/MLD Admin mode | [optional] 
**proxy_querier_admin_mode** | **str** | IGMP/MLD Proxy Querier Admin Mode | [optional] 
**flood_all_unknown_port** | **str** | Flood unknown multicast traffic to all ports. | [optional] 
**control_frames** | **int** | Number of multicast control frames processed by the CPU. | [optional] 
**forwarded_frames** | **int** | Number of multicast data frames forwarded by the CPU. | [optional] 

## Example

```python
from openapi_client.models.snooping_config_get import SnoopingConfigGet

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingConfigGet from a JSON string
snooping_config_get_instance = SnoopingConfigGet.from_json(json)
# print the JSON string representation of the object
print(SnoopingConfigGet.to_json())

# convert the object into a dict
snooping_config_get_dict = snooping_config_get_instance.to_dict()
# create an instance of SnoopingConfigGet from a dict
snooping_config_get_from_dict = SnoopingConfigGet.from_dict(snooping_config_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


