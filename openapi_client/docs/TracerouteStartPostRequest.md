# TracerouteStartPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traceroute_start** | [**TracerouteStart**](TracerouteStart.md) |  | [optional]

## Example

```python
from openapi_client.models.traceroute_start_post_request import TracerouteStartPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteStartPostRequest from a JSON string
traceroute_start_post_request_instance = TracerouteStartPostRequest.from_json(json)
# print the JSON string representation of the object
print(TracerouteStartPostRequest.to_json())

# convert the object into a dict
traceroute_start_post_request_dict = traceroute_start_post_request_instance.to_dict()
# create an instance of TracerouteStartPostRequest from a dict
traceroute_start_post_request_from_dict = TracerouteStartPostRequest.from_dict(traceroute_start_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
