# SwPortstatsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**switch_stats_port** | [**SwPortstats**](SwPortstats.md) |  | [optional] 

## Example

```python
from openapi_client.models.sw_portstats_get200_response import SwPortstatsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortstatsGet200Response from a JSON string
sw_portstats_get200_response_instance = SwPortstatsGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwPortstatsGet200Response.to_json())

# convert the object into a dict
sw_portstats_get200_response_dict = sw_portstats_get200_response_instance.to_dict()
# create an instance of SwPortstatsGet200Response from a dict
sw_portstats_get200_response_from_dict = SwPortstatsGet200Response.from_dict(sw_portstats_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


