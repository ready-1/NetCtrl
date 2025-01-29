# PingTestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | Ping Test State:   * &#x60;0&#x60; &#x3D; PT_SUCCESS   * &#x60;1&#x60; &#x3D; PT_IN_PROGRESS   * &#x60;2&#x60; &#x3D; PT_FAILURE  | [optional] 
**ping_msg** | **str** | Response for Ping message. | [optional] 

## Example

```python
from openapi_client.models.ping_test_status import PingTestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PingTestStatus from a JSON string
ping_test_status_instance = PingTestStatus.from_json(json)
# print the JSON string representation of the object
print(PingTestStatus.to_json())

# convert the object into a dict
ping_test_status_dict = ping_test_status_instance.to_dict()
# create an instance of PingTestStatus from a dict
ping_test_status_from_dict = PingTestStatus.from_dict(ping_test_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


