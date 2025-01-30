# SnoopingConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Snooping family |
**admin_mode** | **str** | IGMP/MLD Admin mode |
**proxy_querier_admin_mode** | **str** | IGMP/MLD Proxy Querier Admin Mode |
**flood_all_unknown_port** | **str** | Flood unknown multicast traffic to all ports. |

## Example

```python
from openapi_client.models.snooping_config_post import SnoopingConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingConfigPost from a JSON string
snooping_config_post_instance = SnoopingConfigPost.from_json(json)
# print the JSON string representation of the object
print(SnoopingConfigPost.to_json())

# convert the object into a dict
snooping_config_post_dict = snooping_config_post_instance.to_dict()
# create an instance of SnoopingConfigPost from a dict
snooping_config_post_from_dict = SnoopingConfigPost.from_dict(snooping_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
