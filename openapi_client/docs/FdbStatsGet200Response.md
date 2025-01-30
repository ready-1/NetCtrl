# FdbStatsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**fdb_stats** | [**FdbStatsGet**](FdbStatsGet.md) |  | [optional]

## Example

```python
from openapi_client.models.fdb_stats_get200_response import FdbStatsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FdbStatsGet200Response from a JSON string
fdb_stats_get200_response_instance = FdbStatsGet200Response.from_json(json)
# print the JSON string representation of the object
print(FdbStatsGet200Response.to_json())

# convert the object into a dict
fdb_stats_get200_response_dict = fdb_stats_get200_response_instance.to_dict()
# create an instance of FdbStatsGet200Response from a dict
fdb_stats_get200_response_from_dict = FdbStatsGet200Response.from_dict(fdb_stats_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
