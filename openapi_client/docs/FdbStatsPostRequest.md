# FdbStatsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdb_stats** | [**FdbStatsPost**](FdbStatsPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.fdb_stats_post_request import FdbStatsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FdbStatsPostRequest from a JSON string
fdb_stats_post_request_instance = FdbStatsPostRequest.from_json(json)
# print the JSON string representation of the object
print(FdbStatsPostRequest.to_json())

# convert the object into a dict
fdb_stats_post_request_dict = fdb_stats_post_request_instance.to_dict()
# create an instance of FdbStatsPostRequest from a dict
fdb_stats_post_request_from_dict = FdbStatsPostRequest.from_dict(fdb_stats_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


