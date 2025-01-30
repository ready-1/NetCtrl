# SnoopingQueriersPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Configured IP address of querier |
**admin_mode** | **str** | Enable or disable querier |
**expiry_interval** | **int** | Expiry interval of a snoop instance in seconds |
**query_interval** | **int** | Snooping query interval in seconds |
**querier_version** | **int** | Configured version for the querier |
**vlan_address** | **str** | IP address configured for the querier |

## Example

```python
from openapi_client.models.snooping_queriers_post import SnoopingQueriersPost

# TODO update the JSON string below
json = "{}"
# create an instance of SnoopingQueriersPost from a JSON string
snooping_queriers_post_instance = SnoopingQueriersPost.from_json(json)
# print the JSON string representation of the object
print(SnoopingQueriersPost.to_json())

# convert the object into a dict
snooping_queriers_post_dict = snooping_queriers_post_instance.to_dict()
# create an instance of SnoopingQueriersPost from a dict
snooping_queriers_post_from_dict = SnoopingQueriersPost.from_dict(snooping_queriers_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
