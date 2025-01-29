# StpPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spanning_tree** | [**Stp**](Stp.md) |  | [optional] 

## Example

```python
from openapi_client.models.stp_post_request import StpPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StpPostRequest from a JSON string
stp_post_request_instance = StpPostRequest.from_json(json)
# print the JSON string representation of the object
print(StpPostRequest.to_json())

# convert the object into a dict
stp_post_request_dict = stp_post_request_instance.to_dict()
# create an instance of StpPostRequest from a dict
stp_post_request_from_dict = StpPostRequest.from_dict(stp_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


