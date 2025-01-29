# FdbStatsGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_entries** | **int** | Count of the static entries in the FDB table. | [optional] 
**dynamic_entries** | **int** | Count of the dynamic entries in the FDB table. | [optional] 
**max_table_entries** | **int** | Maximum number of entries FDB table can hold. | [optional] 
**current_table_entries** | **int** | Current number of entries in the FDB table. | [optional] 
**greatest_table_entries** | **int** | Greatest number of entries the FDB table held. | [optional] 

## Example

```python
from openapi_client.models.fdb_stats_get import FdbStatsGet

# TODO update the JSON string below
json = "{}"
# create an instance of FdbStatsGet from a JSON string
fdb_stats_get_instance = FdbStatsGet.from_json(json)
# print the JSON string representation of the object
print(FdbStatsGet.to_json())

# convert the object into a dict
fdb_stats_get_dict = fdb_stats_get_instance.to_dict()
# create an instance of FdbStatsGet from a dict
fdb_stats_get_from_dict = FdbStatsGet.from_dict(fdb_stats_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


