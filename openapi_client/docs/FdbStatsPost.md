# FdbStatsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**greatest_table_entries_reset** | **bool** | Reset the greatest number of entries in the forwarding database to zero. |

## Example

```python
from openapi_client.models.fdb_stats_post import FdbStatsPost

# TODO update the JSON string below
json = "{}"
# create an instance of FdbStatsPost from a JSON string
fdb_stats_post_instance = FdbStatsPost.from_json(json)
# print the JSON string representation of the object
print(FdbStatsPost.to_json())

# convert the object into a dict
fdb_stats_post_dict = fdb_stats_post_instance.to_dict()
# create an instance of FdbStatsPost from a dict
fdb_stats_post_from_dict = FdbStatsPost.from_dict(fdb_stats_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
