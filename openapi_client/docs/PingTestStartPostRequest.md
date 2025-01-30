# PingTestStartPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ping_test** | [**PingTestStart**](PingTestStart.md) |  | [optional]

## Example

```python
from openapi_client.models.ping_test_start_post_request import PingTestStartPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PingTestStartPostRequest from a JSON string
ping_test_start_post_request_instance = PingTestStartPostRequest.from_json(json)
# print the JSON string representation of the object
print(PingTestStartPostRequest.to_json())

# convert the object into a dict
ping_test_start_post_request_dict = ping_test_start_post_request_instance.to_dict()
# create an instance of PingTestStartPostRequest from a dict
ping_test_start_post_request_from_dict = PingTestStartPostRequest.from_dict(ping_test_start_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
