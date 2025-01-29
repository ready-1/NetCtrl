# MstiPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot1s_msti_entries** | [**MstiPost**](MstiPost.md) |  | [optional] 

## Example

```python
from openapi_client.models.msti_post_request import MstiPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MstiPostRequest from a JSON string
msti_post_request_instance = MstiPostRequest.from_json(json)
# print the JSON string representation of the object
print(MstiPostRequest.to_json())

# convert the object into a dict
msti_post_request_dict = msti_post_request_instance.to_dict()
# create an instance of MstiPostRequest from a dict
msti_post_request_from_dict = MstiPostRequest.from_dict(msti_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


