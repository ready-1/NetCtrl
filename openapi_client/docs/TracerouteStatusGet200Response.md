# TracerouteStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**traceroute_info** | [**TracerouteStatus**](TracerouteStatus.md) |  | [optional]

## Example

```python
from openapi_client.models.traceroute_status_get200_response import TracerouteStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteStatusGet200Response from a JSON string
traceroute_status_get200_response_instance = TracerouteStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(TracerouteStatusGet200Response.to_json())

# convert the object into a dict
traceroute_status_get200_response_dict = traceroute_status_get200_response_instance.to_dict()
# create an instance of TracerouteStatusGet200Response from a dict
traceroute_status_get200_response_from_dict = TracerouteStatusGet200Response.from_dict(traceroute_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
