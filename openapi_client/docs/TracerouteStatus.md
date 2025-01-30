# TracerouteStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | Traceroute Test State:   * &#x60;0&#x60; &#x3D; PT_SUCCESS   * &#x60;1&#x60; &#x3D; PT_IN_PROGRESS   * &#x60;2&#x60; &#x3D; PT_FAILURE  | [optional]
**traceroute_msg** | **str** | Response message for traceroute | [optional]

## Example

```python
from openapi_client.models.traceroute_status import TracerouteStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteStatus from a JSON string
traceroute_status_instance = TracerouteStatus.from_json(json)
# print the JSON string representation of the object
print(TracerouteStatus.to_json())

# convert the object into a dict
traceroute_status_dict = traceroute_status_instance.to_dict()
# create an instance of TracerouteStatus from a dict
traceroute_status_from_dict = TracerouteStatus.from_dict(traceroute_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
